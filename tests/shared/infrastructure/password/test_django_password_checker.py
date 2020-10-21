
import unittest
import pytest

from unittest.mock import Mock

from src.shared.infrastructure.passwords.django import PasswordChecker as DjangoPasswordChecker


def test_django_checker_executed():
    mock = Mock()
    mock.return_value = True
    password, encoded_password = (
        'password',
        'argon2$argon2i$v=19$m=512,t=2,p=2$UGNCM283Nms5TzhP$DmLb3oxgQ0OyCjJSrAtvzg',
    )
    django_password_checker = DjangoPasswordChecker(mock)
    django_password_checker.check_password(password, encoded_password)
    mock.assert_called_with(password, encoded_password)


def test_django_checker_true():
    mock_return = True
    mock = Mock()
    mock.return_value = mock_return
    password, encoded_password = (
        'password',
        'argon2$argon2i$v=19$m=512,t=2,p=2$UGNCM283Nms5TzhP$DmLb3oxgQ0OyCjJSrAtvzg',
    )
    django_password_checker = DjangoPasswordChecker(mock)
    result = django_password_checker.check_password(password, encoded_password)
    assert result == mock_return


def test_django_checker_false():
    mock_return = False
    mock = Mock()
    mock.return_value = mock_return
    password, encoded_password = (
        'password',
        'argon2$argon2i$v=19$m=512,t=2,p=2$UGNCM283Nms5TzhP$DmLb3oxgQ0OyCjJSrAtvzg',
    )
    django_password_checker = DjangoPasswordChecker(mock)
    result = django_password_checker.check_password(password, encoded_password)
    assert result == mock_return


def test_django_checker_non_string_password():
    mock_return = False
    mock = Mock()
    mock.return_value = mock_return
    password, encoded_password = (
        b'password',
        'argon2$argon2i$v=19$m=512,t=2,p=2$UGNCM283Nms5TzhP$DmLb3oxgQ0OyCjJSrAtvzg',
    )
    django_password_checker = DjangoPasswordChecker(mock)
    with pytest.raises(ValueError, match="Password is not string"):
        django_password_checker.check_password(password, encoded_password)


def test_django_checker_non_string_encoded_password():
    mock_return = False
    mock = Mock()
    mock.return_value = mock_return
    password, encoded_password = (
        'password',
        b'argon2$argon2i$v=19$m=512,t=2,p=2$UGNCM283Nms5TzhP$DmLb3oxgQ0OyCjJSrAtvzg',
    )
    django_password_checker = DjangoPasswordChecker(mock)
    with pytest.raises(ValueError, match="Password is not encoded"):
        django_password_checker.check_password(password, encoded_password)
