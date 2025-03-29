from kink import di

from src.services.account_management.repositories.user import IUserRepository
from src.services.service_management.infrastructure.repositories.sql_alchemy.user_service import \
    SQLAlchemyUserServiceRepository
from src.services.service_management.infrastructure.repositories.user_service import IUserServiceRepository
from src.shared.logger.advanced_logger import AdvancedLogger
from src.shared.logger.logger_interface import ICustomLogger


class Bootstrap:
    def __init__(self):
        self.__logger = AdvancedLogger()
        self.__setup_logger()
        self.__define_models()

    def __setup_logger(self):
        di[ICustomLogger] = self.__logger

    def __define_models(self):
        di[IUserRepository] = IUserRepository
        di[IUserServiceRepository] = SQLAlchemyUserServiceRepository
