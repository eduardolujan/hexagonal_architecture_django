from src.shared.infrastructure.log.pylogger_service import get_logger


log = get_logger(file_path=__file__)


class BasicException(Exception):
    """
    BasicException
    """
    def __init__(self, message=None, error=None, errors=None):
        if type(message) is not str:
            raise ValueError("Not valid message")

        super(BasicException, self).__init__()
        self.message = message
        self.errors = error
        self.error = errors


