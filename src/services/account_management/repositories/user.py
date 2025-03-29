from abc import ABC, abstractmethod

from src.infrastructure.db_manager.db_management import AsyncDatabaseManager
from src.services.account_management.domain.user import UserEntity


class IUserRepository(ABC):

    @abstractmethod
    async def create(self, user):
        raise NotImplementedError

    @abstractmethod
    async def get(self, user):
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
    async def is_exist(self, user):
        raise NotImplementedError

    @abstractmethod
    def user_repo(self, session: AsyncDatabaseManager) -> 'IUserRepository':
        raise NotImplementedError