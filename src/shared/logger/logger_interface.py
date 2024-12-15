import uuid
from abc import abstractmethod
from typing import Type

NOTE = "Use a subclass of CustomLogger"

class ICustomLogger:

    @abstractmethod
    def info(self, msg: str, trace_id=str(uuid.uuid4())):
        raise NotImplementedError(NOTE)

    @abstractmethod
    def error(self, msg, exception=Type[Exception], trace_id=str(uuid.uuid4())):
        raise NotImplementedError(NOTE)

    @abstractmethod
    def warning(self, msg, trace_id=str(uuid.uuid4())):
        raise NotImplementedError(NOTE)

    @abstractmethod
    def debug(self, msg, trace_id=str(uuid.uuid4())):
        raise NotImplementedError(NOTE)