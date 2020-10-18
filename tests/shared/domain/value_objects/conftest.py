

from unittest.mock import Mock

import pytest


@pytest.fixture
def setup_email_validator_return_mock():
    def fixture(is_valid=True):
        if type(is_valid) is not bool:
            raise ValueError("Is invalid email")
        email_validator = Mock()
        email_validator.validate_email = Mock()
        email_validator.validate_email.return_value = is_valid
        return email_validator
    return fixture
