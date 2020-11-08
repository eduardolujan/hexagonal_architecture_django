

import pytest
from unittest.mock import Mock

from modules.shared.domain.entities import Entity


class TestEntity(Entity):
    username: str = 'username'
    password: str = 'password'


@pytest.fixture
def setup_orm_manager_get():
    """
    Setup orm manager for get
    """
    def wrapper():
        """
        Wrapper
        """
        mock_model = Mock()
        mock_model.objects = Mock()
        mock_model.objects.filter = Mock()
        mock_model.objects.filter.return_value = TestEntity()
        return mock_model
    return wrapper


@pytest.fixture
def setup_orm_manager_entity():
    def wrapper():
        return TestEntity
    return wrapper
