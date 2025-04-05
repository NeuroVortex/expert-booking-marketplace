from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.shared.account.user import UserEntity
from src.services.service_management.domain.entities.service import ServiceEntity
from src.services.service_management.domain.entities.user_service import UserServiceEntity


class IUserServiceRepository(ABC):

    @abstractmethod
    async def add(self, user_services: list[UserServiceEntity]):
        raise NotImplementedError

    @abstractmethod
    async def remove(self, user_id, public_service_id):
        raise NotImplementedError

    @abstractmethod
    async def get_by_service_public_id(self, public_id) -> list[UserEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_user(self, user) -> list[ServiceEntity]:
        raise NotImplementedError

    @classmethod
    def user_service_repo(cls, session: AsyncSession) -> 'IUserServiceRepository':
        raise NotImplementedError
