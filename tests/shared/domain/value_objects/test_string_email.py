
from unittest.mock import Mock

import pytest
from src.shared.domain.value_objects import Email


def test_value_object_email_success_happy_path(setup_email_validator_return_mock):
    email = 'email@server.mx'
    is_valid = True
    email_validator = setup_email_validator_return_mock(is_valid)
    Email(email, email_validator=email_validator)
    email_validator.validate_email.assert_called_with(email)


def test_value_object_email_success_check_email(setup_email_validator_return_mock):
    email = 'email@server.mx'
    is_valid = True
    email_validator = setup_email_validator_return_mock(is_valid)
    value_object_email = Email(email, email_validator=email_validator)
    assert email == value_object_email.value


def test_value_object_wrong_email_address(setup_email_validator_return_mock):
    email = 'email@server'
    is_valid = False
    email_validator = setup_email_validator_return_mock(is_valid)
    with pytest.raises(ValueError, match="Is not a valid email"):
        Email(email, email_validator=email_validator)


def test_value_object_email_set_value(setup_email_validator_return_mock):
    email = 'email@server.mx'
    is_valid = True
    email_validator = setup_email_validator_return_mock(is_valid)
    with pytest.raises(ValueError, match="You can't assign value"):
        value_object_email = Email(email, email_validator=email_validator)
        value_object_email.value = 'email2@server.mx'


def test_value_object_email_input_value(setup_email_validator_return_mock, subtests):
    values_to_test = [1, 3.0, False, (1, 2, ), [1, 2, 3]]
    is_valid = True
    email_validator = setup_email_validator_return_mock(is_valid)
    for index, value in enumerate(values_to_test):
        with subtests.test(msg=f"Testing {type(value)}:{value}", i=index):
            with pytest.raises(ValueError, match="Email value not string"):
                Email(value, email_validator=email_validator)

