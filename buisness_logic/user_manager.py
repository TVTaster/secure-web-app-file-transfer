from fastapi.security import HTTPBasicCredentials

from model.authentication.user import UserType


class UserManager:

    @staticmethod
    def is_sender(credentials: HTTPBasicCredentials) -> None:
        pass

    @staticmethod
    def is_receiver(credentials: HTTPBasicCredentials) -> None:
        pass


def valid_credentials(credentials: HTTPBasicCredentials, user_type: UserType) -> None:
    pass
