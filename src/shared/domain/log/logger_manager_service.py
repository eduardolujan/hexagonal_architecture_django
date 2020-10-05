from abc import ABC, abstractmethod


class LoggerService(ABC):
    @abstractmethod
    def info(self, message: str):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def error(self, message: str):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def exception(self, message: str):
        raise NotImplementedError("Not implemented yet")
