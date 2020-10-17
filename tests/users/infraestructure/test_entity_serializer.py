


import unittest
import pytest
from unittest.mock import Mock

from src.users.infrastructure.serializers.django import UserEntitySerializer


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
        self._data = _data


class TestUserSerializer(unittest.TestCase):
    def test_entity_serializer(self):
        data = {
            "username": "username",
            "password": "password"
        }
        stub = StubDjangoUserSerializer
        entity_serializer = UserEntitySerializer(stub)
        entity_serializer.get_dto(data)






