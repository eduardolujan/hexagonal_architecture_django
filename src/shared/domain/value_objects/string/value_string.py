# -*- utf-8  -*-


class String:
    __slots__ = ['__value']

    def __init__(self, value):
        self.__value = value

    def __deepcopy__(self, memodict={}):
        return self.__value

    def __repr__(self):
        return self

    def __str__(self):
        return self

    @property
    def value(self):
        return str(self.__value)

    @value.setter
    def value(self):
        raise ValueError("You can't assign value")
