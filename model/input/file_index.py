from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status


class FileIndex(BaseModel):
    index: int


