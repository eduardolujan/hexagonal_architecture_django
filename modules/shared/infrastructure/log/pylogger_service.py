

import os
import logging

from modules.shared.domain.log import Logger


def get_logger(file_path=__file__):
    """
    Get logger function by file path
    @param file_path: Path
    @return: Log instance
    """
    if not os.path.exists(file_path):
        raise ValueError("Path doesn't exists please verify")
    logging.basicConfig()
    log = logging.getLogger(os.path.basename(file_path))
    log.setLevel(logging.DEBUG)
    return log


class PyLoggerService(Logger):
    def __init__(self, file_path=__file__):
        if type(file_path) is not str:
            raise ValueError(f"Parameter file_path is not string {file_path}")

        self.__file_path = file_path
        self.__log = get_logger(self.__file_path)

    def info(self, message: str):
        self.__log.info(message)

    def error(self, message: str):
        self.__log.error(message)

    def exception(self, message: str):
        self.__log.exception(message)
