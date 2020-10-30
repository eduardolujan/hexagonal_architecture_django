from src.shared.infrastructure.log.pylogger_service import get_logger


log = get_logger(file_path=__file__)


class BasicException(Exception):
    """
    BasicException
    """
    def __init__(self, message, error=None, errors=None):
        if not str:
            raise ValueError("You need assign a message")

        if type(message) is not str:
            raise ValueError("Not valid message")

        if not isinstance(error, Exception):
            raise ValueError("Not valid value error this need to be a Exception instance")

        super(BasicException, self).__init__()
        self.__message = message
        self.__error = error
        self.__errors = errors

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.__message

