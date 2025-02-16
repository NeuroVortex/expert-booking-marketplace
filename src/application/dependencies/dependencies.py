import pykka
from kink import di, inject

from src.shared.logger.logger_interface import ICustomLogger


@inject
class Dependencies:
    DependencyInjector = None

    def __init__(self, logger: ICustomLogger):
        self.db_connection = None
        self.__logger = logger
        self.__setup_dependencies()
        Dependencies.DependencyInjector = self

    def __setup_dependencies(self):
        di[ICustomLogger] = self.__logger

    def logger(self) -> ICustomLogger:
        return self.__logger
