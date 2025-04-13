from src.services.account_management.infrastructure.repositories.user_address import IUserAddressRepository


class UserAddressHandler:
    def __init__(self, user_address_repo: IUserAddressRepository):
        self.__user_address_repo = user_address_repo

    def