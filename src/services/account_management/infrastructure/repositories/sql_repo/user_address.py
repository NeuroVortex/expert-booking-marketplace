from src.services.account_management.domain.address import AddressEntity
from src.services.account_management.infrastructure.repositories.user_address import IUserAddressRepository
from src.shared.account.user import UserEntity


class SqlAlchemyUserAddressRepository(IUserAddressRepository):
    def create(self, address: AddressEntity):
        pass

    def get_by_user(self, user: UserEntity):
        pass

    def update(self, address: AddressEntity):
        pass

    def delete(self, address: AddressEntity):
        pass