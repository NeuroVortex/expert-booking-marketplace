from src.services.account_management.domain.user import UserEntity
from src.services.account_management.repositories.user import IUserRepository


class UserHandler:
    def __init__(self, user_repository: IUserRepository):
        self.__user_repo = user_repository

    def add_user(self, user_dto) -> UserEntity:
        pass

    def get_user(self, user_public_id: str) -> UserEntity:
        pass

    def remove_user(self, user_public_id: str) -> bool:
        pass
