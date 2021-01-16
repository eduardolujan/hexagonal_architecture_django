from abc import ABC, abstractmethod


class Environ(ABC):
    """
    Environ
    """

    def get(self, key, default=None):
        """
        Get str value
        @return: str
        @rtype: str
        """
        raise NotImplementedError("Not implemented error")

    def get_str(self, key, default=None):
        """
        Get str value
        @return: str
        @rtype: str
        """
        raise NotImplementedError("Not implemented error")

    def get_int(self, key, default=None):
        """
        Get int value
        @return: int
        @rtype: int
        """
        raise NotImplementedError("Not implemented error")

    def get_float(self, key, default=None):
        """
        Get int value
        @return: int
        @rtype: int
        """
        raise NotImplementedError("Not implemented error")

    def get_list(self, key, default=list()):
        """
        Get list value
        @return: list
        @rtype: list
        """
        raise NotImplementedError("Not implemented error")

    def get_list(self, key, default=tuple()):
        """
        Get tuple value
        @return: tuple
        @rtype: tuple
        """
        raise NotImplementedError("Not implemented error")
