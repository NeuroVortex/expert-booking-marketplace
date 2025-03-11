from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.services.service_management.domain.service import ServiceEntity


class IServiceRepository(ABC):

    @abstractmethod
    async def add(self, service: ServiceEntity) -> str:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, service_public_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def update(self, service: ServiceEntity) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, service_id: int) -> ServiceEntity | None:
        raise NotImplementedError

    @abstractmethod
    async def get_by_public_id(self, service_identifier: str) -> ServiceEntity | None:
        raise NotImplementedError

    @abstractmethod
    async def get_children(self, parent_id: int) -> list[ServiceEntity]:
        raise NotImplementedError

    @abstractmethod
    async def get_parents(self) -> list[ServiceEntity]:
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self) -> list[ServiceEntity]:
        raise NotImplementedError

    @classmethod
    def service_repo(cls, session: AsyncSession) -> 'IServiceRepository':
        raise NotImplementedError


