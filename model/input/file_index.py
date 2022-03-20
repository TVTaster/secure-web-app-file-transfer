from fastapi import HTTPException
from pydantic import BaseModel, validator
from starlette import status


class FileIndex(BaseModel):
    index: int

    @validator('index')
    def index_length_validation(cls, index) -> int:
        if len(str(index)) != 6:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='index number must be exactly 6 digits')
        return index
