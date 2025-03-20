from abc import ABC, abstractmethod

from src.services.account_management.domain.user import UserEntity
from src.services.service_management.domain.entities.service import ServiceEntity


class IUserServiceRepository(ABC):

    @abstractmethod
    async def add(self, user_id, service_id):
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
