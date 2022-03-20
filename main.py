import uvicorn
from fastapi import FastAPI, UploadFile, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from starlette.responses import HTMLResponse


app = FastAPI()
security = HTTPBasic()


@app.get("/")
async def root():
    with open("html/dist/index.html", "r") as html_file:
        html = html_file.read()
    return HTMLResponse(html)


@app.get("/api/v1/files/{index}")
async def file_request(index: int,
                       credentials: HTTPBasicCredentials = Depends(security)) -> str:
    pass

@app.post("/api/v1/files")
async def upload_file(file: UploadFile,
                      credentials: HTTPBasicCredentials = Depends(security)) -> int:
    pass

@app.get("/health")
async def health():
    return "version 1.0"


if __name__ == '__main__':
    uvicorn.run(app)
