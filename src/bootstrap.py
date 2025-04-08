from kink import di

from src.application.logger.logger_interface import ICustomLogger
from src.services.account_management.infrastructure.repositories.sql_repo.user import SqlAlchemyUserRepository
from src.services.account_management.infrastructure.repositories.user import IUserRepository
from src.services.service_management.infrastructure.repositories.service import IServiceRepository
from src.services.service_management.infrastructure.repositories.sql_alchemy.service import SQLAlchemyServiceRepository
from src.services.service_management.infrastructure.repositories.sql_alchemy.user_service import \
    SQLAlchemyUserServiceRepository
from src.services.service_management.infrastructure.repositories.user_service import IUserServiceRepository
from src.application.logger.advanced_logger import AdvancedLogger


class Bootstrap:
    def __init__(self):
        self.__logger = AdvancedLogger()
        self.__setup_logger()
        self.__define_models()

    def __setup_logger(self):
        di[ICustomLogger] = self.__logger

    @classmethod
    def __define_models(cls):
        di[IServiceRepository] = SQLAlchemyServiceRepository
        di[IUserRepository] = SqlAlchemyUserRepository
        di[IUserServiceRepository] = SQLAlchemyUserServiceRepository
