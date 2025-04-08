from src.schema.user import GetUser
from src.shared.account.user import UserEntity


class ToGetUsers:
    def __rmatmul__(self, user: UserEntity):
        return GetUser()