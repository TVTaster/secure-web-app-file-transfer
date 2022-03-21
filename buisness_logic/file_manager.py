import glob
from pathlib import PurePath, Path
from uuid import uuid4

import aiofiles
from fastapi import HTTPException, UploadFile

from configuration.constants import local_directory_base_storage
from configuration.yaml_config import Configuration
from model.input.file_index import FileIndex
from utils.cache import timed_lru_cache

configuration = Configuration.read()


class FileManager:
    base_storage: str = configuration[local_directory_base_storage]

    @staticmethod
    @timed_lru_cache
    def retrieve_file(index: FileIndex) -> str:
        file_path = PurePath(FileManager.base_storage).joinpath(str(index.index))

        if not Path.exists(Path(file_path)):
            raise HTTPException(status_code=404, detail="The requested file not found")

        found_file = glob.glob(str(file_path) + "/*")[0]
        with open(found_file) as file:
            return file.read()

    @staticmethod
    async def save_file(file: UploadFile) -> int:
        new_index = int(str(uuid4().int)[:6])
        file_path = PurePath(FileManager.base_storage).joinpath(str(new_index))

        # In any case the new hashed 6 digit already benn used
        # keep searching until find brand new un unused index
        while Path.exists(Path(file_path)):
            new_index = int(str(uuid4().int)[:6])
            file_path = PurePath(FileManager.base_storage).joinpath(str(new_index))

        Path.mkdir(Path(file_path))

        async with aiofiles.open(file_path.joinpath(file.filename), 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)

        return new_index
