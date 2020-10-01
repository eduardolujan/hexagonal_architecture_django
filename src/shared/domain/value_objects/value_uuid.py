# -*- utf-8  -*-


from abc import ABC
from uuid import UUID


class Uuid(ABC):
    """
    UUID 4
    """
    def __init__(self, value, field_name='id'):
        self.__value = UUID(value, version=4)
        self.__field_name = field_name

    def __deepcopy__(self, memodict={}):
        return self.__value

    def __repr__(self):
        return str(self.__value)

    @property
    def uuid(self):
        return self.__value

    def as_dict(self):
        _dict = dict()
        _dict[self.__field_name] = self.__value
        return _dict
