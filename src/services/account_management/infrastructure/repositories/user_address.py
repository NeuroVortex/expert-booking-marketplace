from abc import ABC, abstractmethod

from src.services.account_management.domain.address import AddressEntity
from src.shared.account.user import UserEntity


class IUserAddressRepository(ABC):

    @abstractmethod
    def create(self, address: AddressEntity):
        raise NotImplementedError

    @abstractmethod
    def get_by_user(self, user: UserEntity):
        raise NotImplementedError

    @abstractmethod
    def update(self, address: AddressEntity):
        raise NotImplementedError

    @abstractmethod
    def delete(self, address: AddressEntity):
        raise NotImplementedError
