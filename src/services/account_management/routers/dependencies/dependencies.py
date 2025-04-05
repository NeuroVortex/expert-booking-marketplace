from kink import di

from src.services.account_management.application.handler.user import UserHandler
from src.services.account_management.infrastructure.repositories.sql_repo.user import SqlAlchemyUserRepository
from src.services.account_management.infrastructure.repositories.user import IUserRepository


class Dependencies:
    Dependency = None

    def __init__(self):
        di[IUserRepository] = SqlAlchemyUserRepository
        Dependencies.Dependency = self

    @classmethod
    def user_handler(cls) -> UserHandler:
        return UserHandler()
