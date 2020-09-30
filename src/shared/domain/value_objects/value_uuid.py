# -*- utf-8  -*-


from abc import ABC
from uuid import UUID


class Uuid(ABC):
    """
    UUID 4
    """
    def __init__(self, value):
        self.__value = UUID(value, version=4)

    def __deepcopy__(self, memodict={}):
        return self.__value

    def __repr__(self):
        return str(self.__value)

    @property
    def uuid(self):
        return self.__value
