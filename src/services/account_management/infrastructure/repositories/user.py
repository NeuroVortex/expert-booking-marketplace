from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.shared.account.user import UserEntity


class IUserRepository(ABC):

    @abstractmethod
    async def create(self, user: UserEntity) -> str:
        raise NotImplementedError

    @abstractmethod
    async def remove(self, user_public_id: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    async def get_by_phone(self, phone: str):
        raise NotImplementedError

    @abstractmethod
    async def get_by_email(self, email: str):
        raise NotImplementedError

    @abstractmethod
    async def get_by_identification(self, identification: str):
        raise NotImplementedError

    @abstractmethod
    async def get_by_user_public_id(self, public_id: str) -> UserEntity:
        raise NotImplementedError

    @abstractmethod
    async def update(self, user):
        raise NotImplementedError

    @abstractmethod
    async def is_exist(self, user: UserEntity) -> bool:
        raise NotImplementedError

    @classmethod
    def user_repo(cls, session: AsyncSession) -> 'IUserRepository':
        raise NotImplementedError