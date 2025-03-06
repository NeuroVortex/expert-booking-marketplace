from abc import ABC, abstractmethod


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
    async def update(self, user):
        raise NotImplementedError
