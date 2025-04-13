from abc import ABC, abstractmethod


class IUserPaymentRepository(ABC):

    @abstractmethod
    def create(self, user, payment):
        raise NotImplementedError

    @abstractmethod
    def get_by_user(self, user):
        raise NotImplementedError

    @abstractmethod
    def update(self, user, payment):
        raise NotImplementedError

    @abstractmethod
    def delete(self, user, payment):
        raise NotImplementedError
