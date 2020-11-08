
import pytest
from modules.shared.domain.value_objects import String


def test_string_value_object_success():
    value = 'This is value object'
    str_value_object = String(value)
    assert str_value_object.value == value


def test_string_value_object_invalid_int():
    value = 1
    with pytest.raises(ValueError, match="Is not string"):
        String(value)


def test_string_value_object_invalid_float():
    value = 9.99
    with pytest.raises(ValueError, match="Is not string"):
        String(value)

