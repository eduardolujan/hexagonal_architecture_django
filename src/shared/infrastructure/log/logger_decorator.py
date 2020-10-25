# -*- coding: utf-8 -*-


from inspect import isclass
from src.shared.domain.log import Logger


class LoggerDecorator:
    def __init__(self, logger):
        """
        Logger class decorator
        @param file_path: File path to log
        """
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
