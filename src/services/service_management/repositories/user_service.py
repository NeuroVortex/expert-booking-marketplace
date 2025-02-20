from abc import ABC, abstractmethod


class IUserServiceRepository(ABC):

    @abstractmethod
    async def add(self, user, service):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, user, service):
        raise NotImplementedError

    @abstractmethod
    async def get_by_service(self, service):
        raise NotImplementedError

    @abstractmethod
    async def get_by_user(self, user):
        raise NotImplementedError
