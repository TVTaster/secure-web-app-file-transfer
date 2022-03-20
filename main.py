import uvicorn
from fastapi import FastAPI, UploadFile, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from buisness_logic.file_manager import FileManager
from buisness_logic.user_manager import UserManager
from configuration.constants import server_host, server_port, server_reload
from configuration.yaml_config import Configuration
from model.input.file_index import FileIndex

configuration = Configuration.read()

app = FastAPI()
security = HTTPBasic()


@app.get("/")
async def root():
    return f"Please visit swagger at {configuration[server_host]}:{configuration[server_port]}/docs"


@app.get("/api/v1/files/{index}")
async def file_request(index: int,
                       credentials: HTTPBasicCredentials = Depends(security)) -> str:
    UserManager.is_receiver(credentials)
    return FileManager.retrieve_file(FileIndex(index=index))


@app.post("/api/v1/files")
async def upload_file(file: UploadFile,
                      credentials: HTTPBasicCredentials = Depends(security)) -> int:
    UserManager.is_sender(credentials)
    return await FileManager.save_file(file)


@app.get("/health")
async def health():
    return "version 1.0"


if __name__ == '__main__':
    uvicorn.run("main:app",
                host=configuration[server_host],
                port=configuration[server_port],
                reload=configuration[server_reload])
