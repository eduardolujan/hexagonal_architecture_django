
import pytest
from unittest.mock import Mock

from src.shared.infrastructure.passwords.django import PasswordCreator as DjangoPasswordCreator


@pytest.mark.password_creator
def test_password_creator_make_password(get_django_password):
    password, encoded_password = get_django_password()
    django_make_password_mock = Mock()
    django_make_password_mock.return_value = encoded_password
    django_password_creator = DjangoPasswordCreator(django_make_password_mock)
    django_password_creator.create(password)
    django_make_password_mock.assert_called_with(password)


@pytest.mark.password_creator
def test_password_creator_encoded(get_django_password):
    password, encoded_password = get_django_password()
    django_make_password_mock = Mock()
    django_make_password_mock.return_value = encoded_password
    django_password_creator = DjangoPasswordCreator(django_make_password_mock)
    django_password_encoded = django_password_creator.create(password)
    assert encoded_password == django_password_encoded


@pytest.mark.password_creator
def test_django_password_creator_non_string_password(get_django_password):
    _, encoded_password = get_django_password()
    password = b'string'
    django_make_password_mock = Mock()
    django_make_password_mock.return_value = encoded_password
    django_password_checker = DjangoPasswordCreator(django_make_password_mock)
    with pytest.raises(ValueError, match="Password is not string"):
        django_password_checker.create(password)
