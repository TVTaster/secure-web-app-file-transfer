from enum import Enum, auto

from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class UserType(Enum):
    SENDER = auto()
    RECEIVER = auto()
