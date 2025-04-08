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
    async def remove(self, user: UserEntity, services: list[ServiceEntity]):
        raise NotImplementedError

    @abstractmethod
    async def get(self, user_services_public_ids: list[str]) -> list[UserServiceEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_users_by_service_public_id(self, service: ServiceEntity) -> list[UserEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_by_user(self, user: UserEntity) -> list[ServiceEntity]:
        raise NotImplementedError

    @classmethod
    def user_service_repo(cls, session: AsyncSession) -> 'IUserServiceRepository':
        raise NotImplementedError
