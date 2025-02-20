from abc import ABC, abstractmethod


class IUserAddressRepository(ABC):

    @abstractmethod
    def create(self, user, address):
        raise NotImplementedError

    @abstractmethod
    def get_by_user(self, user):
        raise NotImplementedError

    @abstractmethod
    def update(self, user, address):
        raise NotImplementedError

    @abstractmethod
    def delete(self, user, address):
        raise NotImplementedError
