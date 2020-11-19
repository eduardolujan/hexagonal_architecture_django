
from environ import Env

# Domain
from modules.shared.domain.environ import Environ


class DjangoEnviron(Environ):
    """
    Environ
    """
    def __init__(self, environ):
        self.__environ = environ or Env()

    def get(self, key, default=None):
        """
        Get str value
        @return: str
        @rtype: str
        """
        return self.get_str(key, default=default)

    def get_str(self, key, default=None):
        """
        Get str value
        @return: str
        @rtype: str
        """
        return self.__environ.str(key, default=default)

    def get_int(self, key, default=None):
        """
        Get int value
        @return: int
        @rtype: int
        """
        return self.__environ.int(key, default=default)

    def get_float(self, key, default=None):
        """
        Get int value
        @return: int
        @rtype: int
        """
        return self.__environ.float(key, default=default)

    def get_list(self, key, default=list()):
        """
        Get int value
        @return: int
        @rtype: int
        """
        return self.__environ.list(key, default=default)

    def get_tuple(self, key, default=tuple()):
        """
        Get tuple value
        @return: tuple
        @rtype: tuple
        """
        return self.__environ.tuple(key, default=default)


