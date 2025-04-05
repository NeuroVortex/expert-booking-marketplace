from kink import inject

from src.infrastructure.db_manager.sql_alchemy.session import AsyncDatabaseSessionManager
from src.services.account_management.application.exceptions.user import UserExistException
from src.services.account_management.schemas.extensions.user import ToUserEntity
from src.shared.account.user import UserEntity
from src.services.account_management.infrastructure.repositories.user import IUserRepository
from src.services.account_management.schemas.user import UserDto


@inject
class UserHandler:
    def __init__(self, user_repository: IUserRepository):
        self.__user_repo = user_repository

    async def add_user(self, user_dto: UserDto) -> str:
        user: UserEntity = user_dto @ ToUserEntity()
        async with AsyncDatabaseSessionManager() as session:
            is_exist = await self.__user_repo.user_repo(session).is_exist(user)

            if is_exist:
                raise UserExistException()

            else:
                user_public_id = await self.__user_repo.user_repo(session).create(user)

        return user_public_id

    async def get_user(self, user_public_id: str) -> UserEntity:
            async with AsyncDatabaseSessionManager() as session:
                user = await self.__user_repo.user_repo(session).get_by_user_public_id(user_public_id)

            return user

    async def remove_user(self, user_public_id: str) -> bool:
        async with AsyncDatabaseSessionManager() as session:
            await self.__user_repo.user_repo(session).remove(user_public_id)

        return True
