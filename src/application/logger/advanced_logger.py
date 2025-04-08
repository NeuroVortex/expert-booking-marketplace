import logging
import uuid
from typing import Type

from src.app.app_settings import AppSettings
from src.application.logger.logger_interface import ICustomLogger
from advancedLogger import AdvancedLogHandler, AdvancedLogFormatter



class AdvancedLogger(ICustomLogger):
    def __init__(self):
        self.__logger = logging.getLogger(__name__)
        self.__logger.setLevel(logging.DEBUG)
        self.__handler = AdvancedLogHandler()
        self.__handler.setFormatter(AdvancedLogFormatter())
        self.__logger.addHandler(self.__handler)
        self.__console = AppSettings.APP_SETTINGS['loggerConfig']['console']

    def info(self, msg: str, trace_id=str(uuid.uuid4())):
        if self.__console:
            self.__logger.info(msg)

    def error(self, msg, exception=Type[Exception], trace_id=str(uuid.uuid4())):
        if self.__console:
            self.__logger.error(str(exception), msg)

    def warning(self, msg, trace_id=str(uuid.uuid4())):
        if self.__console:
            self.__logger.warning(msg)

    def debug(self, msg, trace_id=str(uuid.uuid4())):
        if self.__console:
            self.__logger.debug(msg)