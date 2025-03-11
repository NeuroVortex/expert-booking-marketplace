from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession

from src.services.service_management.contract.service_dto import ServiceDto


class IServiceRepository(ABC):

    @abstractmethod
    async def add(self, service: ServiceDto) -> str:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, service):
        raise NotImplementedError

    @abstractmethod
    async def update(self, service):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, service_id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_by_public_id(self, service_identifier: str):
        raise NotImplementedError

    @abstractmethod
    async def get_children(self, parent_id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_parents(self):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError

    @classmethod
    def service_repo(cls, session: AsyncSession) -> 'IServiceRepository':
        raise NotImplementedError


