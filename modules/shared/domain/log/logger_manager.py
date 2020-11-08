from abc import ABC, abstractmethod


class Logger(ABC):
    """
    Logger abstract class
    """
    @abstractmethod
    def info(self, message: str) -> None:
        """
        Set info log
        @param message: message to log
        @type message: str
        @return: None
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def error(self, message: str) -> None:
        """
        Set error log
        @param message: message to log
        @type message: str
        @return: None
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def exception(self, message: str) -> None:
        """
        Set exception log
        @param message: message to log
        @type message: str
        @return: None
        """
        raise NotImplementedError("Not implemented yet")
