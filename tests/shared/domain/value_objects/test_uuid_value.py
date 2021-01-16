from unittest.mock import Mock
from uuid import uuid4, UUID as uuid_creator

import pytest
from modules.shared.domain.value_objects import Uuid, String


def test_value_object_uuid_invalid_uuid_v4():
    invalid_uuid_v4 = '16994de6-e9b5-40ed-80e2-8a697db0bed'
    with pytest.raises(ValueError, match="Is invalid UUID v4"):
        Uuid(invalid_uuid_v4)


def test_value_object_uuid_invalid_uuid_v4_as_string():
    invalid_uuid_v4 = 'test'
    with pytest.raises(ValueError, match="Is invalid UUID v4"):
        Uuid(invalid_uuid_v4)


def test_value_object_uuid_invalid_uuid_v4_int():
    invalid_uuid_v4 = 1
    with pytest.raises(ValueError):
        Uuid(invalid_uuid_v4)


def test_value_object_uuid_invalid_uuid_v4_float():
    invalid_uuid_v4 = 2.0
    with pytest.raises(ValueError):
        Uuid(invalid_uuid_v4)


def test_value_object_uuid_v4_is_called():
    uuid_v4 = 'a8024bc1-386b-4251-9f86-a5a1af774553'
    instance_uuid_v4 = uuid_creator(uuid_v4, version=4)
    uuid_v4_mock = Mock()
    uuid_v4_mock.return_value = instance_uuid_v4
    generated_uuid = Uuid(uuid_v4, uuid_generator=uuid_v4_mock)
    assert uuid_v4 == generated_uuid.value


def test_value_object_uuid_v4_is_called_with():
    uuid_v4 = 'a8024bc1-386b-4251-9f86-a5a1af774553'
    instance_uuid_v4 = uuid_creator(uuid_v4, version=4)
    uuid_v4_mock = Mock()
    uuid_v4_mock.return_value = instance_uuid_v4
    Uuid(uuid_v4, uuid_generator=uuid_v4_mock)
    uuid_v4_mock.assert_called_with(uuid_v4, version=4)


@pytest.mark.skip
def test_value_object_uuid_v4_with_v3():
    pass


if __name__ == '__main__':
    test_value_object_uuid_v4_is_called()



