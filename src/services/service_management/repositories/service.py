from abc import ABC, abstractmethod


class IServiceRepository(ABC):

    @abstractmethod
    async def create(self, service):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, service):
        raise NotImplementedError

    @abstractmethod
    async def update(self, service):
        raise NotImplementedError

    @abstractmethod
    async def get(self, service):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, service):
        raise NotImplementedError

    @abstractmethod
    async def get_by_category(self, category):
        raise NotImplementedError
    
    @abstractmethod
    async def get_all(self):
        raise NotImplementedError


