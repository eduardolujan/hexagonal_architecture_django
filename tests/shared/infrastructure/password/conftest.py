import pytest


@pytest.fixture
def get_django_password():
    def wrap():
        password, encoded_password = (
            'password',
            'argon2$argon2i$v=19$m=512,t=2,p=2$UGNCM283Nms5TzhP$DmLb3oxgQ0OyCjJSrAtvzg',
        )
        return password, encoded_password
    return wrap
