

from django.contrib.auth.hashers import make_password

from src.shared.domain.passwords import PasswordGenerator


class DjangoPasswordGenerator(PasswordGenerator):
    def __init__(self):
        pass

    def make(self, password):
        return make_password(password)
