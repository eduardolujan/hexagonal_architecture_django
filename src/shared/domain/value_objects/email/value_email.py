from abc import ABC, abstractmethod

from validate_email import validate_email


class ValidateEmail(ABC):
    @abstractmethod
    def validate_email(self, email):
        raise NotImplementedError("Not implemented error")


class Py3ValidateEmail(ValidateEmail):
    def __init__(self):
        pass

    def validate_email(self, email):
        is_valid = validate_email(email_address=email, check_regex=True, check_mx=False)
        return is_valid

    def __call__(self, email):
        self.validate_email(email)


class Email:
    validate_email = Py3ValidateEmail()

    __slots__ = ['__value']

    def __init__(self, value):
        if not self.validate_email():
            raise Exception('Algo mal')
        self.__value = value

    def __deepcopy__(self, memodict={}):
        return self.__value

    def __repr__(self):
        return str(self.__value)

    @property
    def value(self):
        return str(self.__value)

    @value.setter
    def value(self):
        raise ValueError("You can't assign value")

