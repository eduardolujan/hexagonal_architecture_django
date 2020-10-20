

from django.contrib.auth.hashers import make_password as django_make_password

from src.shared.domain.passwords import PasswordGenerator


class PasswordCreator(PasswordGenerator):
    def __init__(self, _make_password=None):
        self._make_password = _make_password or django_make_password

    def create(self, password):
        if type(password) is not str:
            raise ValueError("Password is not string")
        return self._make_password(password)
