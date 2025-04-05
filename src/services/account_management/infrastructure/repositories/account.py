from abc import ABC, abstractmethod


class IAccountRepository(ABC):

    @abstractmethod
    def create(self, account):
        raise NotImplementedError

    @abstractmethod
    def get(self, account):
        raise NotImplementedError

    @abstractmethod
    def get_by_user(self, user):
        raise NotImplementedError

    @abstractmethod
    def get_by_user_and_platform(self, user, platform):
        raise NotImplementedError

    @abstractmethod
    def update(self, account):
        raise NotImplementedError
