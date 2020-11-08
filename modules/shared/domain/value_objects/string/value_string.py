# -*- utf-8  -*-


class String:

    def __init__(self, value):
        if type(value) is not str:
            raise ValueError(f"Is not string value:{value} type:{type(value)}")

        self.__value = value

    def __deepcopy__(self, memodict={}):
        return self.__value

    def __repr__(self):
        return self.__value

    def __str__(self):
        return self.__value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self):
        raise ValueError("You can't assign value")
