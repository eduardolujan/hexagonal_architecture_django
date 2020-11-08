


import unittest
import pytest
from unittest.mock import Mock

from modules.users.infrastructure.serializers.django import UserSerializer
from modules.shared.infrastructure.serializers.django import SerializerManager


class StubDjangoUserSerializer:

    def __init__(self, data=None, is_valid=True):
        self._data = data
        self._is_valid = is_valid

    def is_valid(self):
        return self._is_valid

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, _data):
        raise Exception("You can't assign value to data")


class TestUserSerializer(unittest.TestCase):
    def test_entity_serializer(self):
        data = {
            "username": "username",
            "password": "password"
        }
        entity_serializer = SerializerManager(StubDjangoUserSerializer)
        user_dto = entity_serializer.get_dto_from_dict(data)
        pass







