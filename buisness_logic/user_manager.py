import secrets

from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

from model.authentication.user import UserType



class UserManager:

    @staticmethod
    def is_sender(credentials: HTTPBasicCredentials) -> None:
        return valid_credentials(credentials, UserType.SENDER)

    @staticmethod
    def is_receiver(credentials: HTTPBasicCredentials) -> None:
        return valid_credentials(credentials, UserType.RECEIVER)


def valid_credentials(credentials: HTTPBasicCredentials, user_type: UserType) -> None:
    if user_type == UserType.RECEIVER:
        username = "tarazan"
        password = "1q2w3e4r"
    else:
        username = "jane"
        password = "q1w2e3r4"

    # using secrets.compare_digest against "Timing Attacks"
    if not (secrets.compare_digest(credentials.username, username) and
            secrets.compare_digest(credentials.password, password)):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
