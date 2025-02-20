from abc import ABC, abstractmethod


class Reservation(ABC):

    @abstractmethod
    async def create(self, reservation):
        raise NotImplementedError

    @abstractmethod
    async def get_by_user(self, user):
        raise NotImplementedError

    @abstractmethod
    async def update(self, reservation):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, reservation):
        raise NotImplementedError
