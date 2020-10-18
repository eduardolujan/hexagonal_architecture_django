from abc import ABC, abstractmethod

from validate_email import validate_email


class EmailValidator(ABC):
    @abstractmethod
    def validate_email(self, email):
        raise NotImplementedError("Not implemented error")


class Py3EmailValidator(EmailValidator):
    def __init__(self):
        pass

    def validate_email(self, email):
        is_valid = validate_email(email_address=email, check_regex=True, check_mx=False)
        return is_valid

    def __call__(self, email):
        self.validate_email(email)


class Email:
    def __init__(self, value, email_validator=None):
        if type(value) is not str:
            raise ValueError("Email value not string")

        self.email_validator = email_validator or Py3EmailValidator()
        if not self.email_validator.validate_email(value):
            raise ValueError("Is not a valid email")

        self.__value = value

    def __deepcopy__(self, memodict={}):
        return self.__value

    def __repr__(self):
        return self.__value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        raise ValueError("You can't assign value")

