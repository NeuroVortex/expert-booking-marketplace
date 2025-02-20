from abc import ABC, abstractmethod


class IServiceCategoryRepository(ABC):

    @abstractmethod
    async def create(self, category):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, category):
        raise NotImplementedError

    @abstractmethod
    async def update(self, category):
        raise NotImplementedError

    @abstractmethod
    async def get_by_id(self, category):
        raise NotImplementedError

    @abstractmethod
    async def get_all(self):
        raise NotImplementedError


