import pytest
from unittest.mock import Mock

from modules.shared.infrastructure.persistence.django import OrmManager


def test_orm_manager_get_entity(setup_orm_manager_get, setup_orm_manager_entity):
    model = setup_orm_manager_get()
    entity_class = setup_orm_manager_entity()
    params = dict(username='test', password='test')
    instance_entity = entity_class(**params)
    orm_manager = OrmManager(model=model, entity=entity_class)
    orm_manager.orm_get(**instance_entity.as_dict())


if __name__ == '__main__':
    pass
    pytest.main(['test_orm_manager.py', "-s"])
