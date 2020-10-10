from functools import wraps
from src.shared.infrastructure.logs import LoggerDecorator, PyLoggerService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class Decorator:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __call__(self, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            self.log.info(f"Fields args: {args}, kwargs: {kwargs}")
            return fn(*args, **kwargs)
        return wrapper


@Decorator(params=[1, 2, 3])
def fun(param1, param2, name='pedro'):
    pass


if __name__ == '__main__':
    fun(1, 2, name='Eduardo')
