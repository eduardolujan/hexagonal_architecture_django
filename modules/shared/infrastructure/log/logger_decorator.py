# -*- coding: utf-8 -*-


from inspect import isclass
from modules.shared.domain.log import Logger


class LoggerDecorator:
    """
    Logger Decorator
    """

    def __init__(self, logger=None):
        """
        Logger class decorator
        @param logger: File path to log
        """
        if logger is None:
            raise ValueError(f"Parameter logger is null is not allowed")

        if not issubclass(logger.__class__, (Logger,)):
            raise ValueError(f"Logger instance is not subclass of LoggerService")

        self.__logger = logger

    def __call__(self, _class):
        """
        Set log variable of log to class
        @param _class: Class to patch
        @return: Class modified
        """
        if not isclass(_class):
            raise Exception(f"The parameter cls is not a class {_class}")

        setattr(_class, 'log', self.__logger)  # Log injection
        return _class
