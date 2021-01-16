# -*- utf-8  -*-

from typing import NoReturn

from uuid import UUID as pyuuid_validator


class Uuid:
    """
    UUID 4
    """

    def __init__(self, value, field_name='id', uuid_generator=None):
        self._field_name = field_name
        self._uuid_generator = uuid_generator or pyuuid_validator
        self._value = self.__validate(value)

    def __deepcopy__(self, memodict={}):
        return self._value

    def __repr__(self):
        return str(self._value or 'None')

    def __validate(self, value) -> NoReturn:

        if type(value) is not str:
            raise ValueError(f"Parameter value:{value} is not string")

        try:
            self._uuid_generator(value, version=4)
        except Exception as err:
            raise ValueError(f"Is invalid UUID v4, value:{value} err:{err}")

    @property
    def value(self):
        return str(self._value)

    @value.setter
    def value(self):
        raise ValueError("You can't assign value")

    def as_dict(self):
        _dict = dict()
        _dict[self._field_name] = self._value
        return _dict


