from fastapi import UploadFile

from model.input.file_index import FileIndex


class FileManager:

    @staticmethod
    def retrieve_file(index: FileIndex) -> str:
        pass

    @staticmethod
    async def save_file(file: UploadFile) -> int:
        pass
