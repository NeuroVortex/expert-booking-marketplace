from kink import di

from src.services.service_management.repositories.service import IServiceRepository
from src.services.service_management.repositories.sql_alchemy.service import SQLAlchemyServiceRepository
from src.shared.logger.advanced_logger import AdvancedLogger
from src.shared.logger.logger_interface import ICustomLogger


class Bootstrap:
    def __init__(self):
        self.__logger = AdvancedLogger()
        self.__setup_logger()

    def __setup_logger(self):
        di[ICustomLogger] = self.__logger

