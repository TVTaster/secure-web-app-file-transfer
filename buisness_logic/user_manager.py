import secrets

from fastapi import HTTPException
from fastapi.security import HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

from configuration.constants import receiver_username, receiver_password, sender_username, sender_password
from configuration.yaml_config import Configuration
from model.authentication.user import UserType

configuration = Configuration.read()


class UserManager:

    @staticmethod
    def is_sender(credentials: HTTPBasicCredentials) -> None:
        return valid_credentials(credentials, UserType.SENDER)

    @staticmethod
    def is_receiver(credentials: HTTPBasicCredentials) -> None:
        return valid_credentials(credentials, UserType.RECEIVER)


def valid_credentials(credentials: HTTPBasicCredentials, user_type: UserType) -> None:
    if user_type == UserType.RECEIVER:
        username = configuration[receiver_username]
        password = configuration[receiver_password]
    else:
        username = configuration[sender_username]
        password = configuration[sender_password]

    # using secrets.compare_digest against "Timing Attacks"
    if not (secrets.compare_digest(credentials.username, username) and
            secrets.compare_digest(credentials.password, password)):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
