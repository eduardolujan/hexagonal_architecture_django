

from django.contrib.auth.hashers import check_password as django_check_password_checker

from src.shared.domain.passwords import PasswordChecker


class DjangoPasswordChecker(PasswordChecker):
    def __init__(self, password_checker=None):
        self._check_password_checker = password_checker or django_check_password_checker

    def check_password(self, password, encoded):
        if type(password) is not str:
            raise ValueError("Password is not string")

        if type(encoded) is not str:
            raise ValueError("Password is not encoded")

        return self._check_password_checker(password, encoded)
