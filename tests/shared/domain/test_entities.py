from uuid import uuid4

import pytest

from src.shared.domain.entity import EntityID


def test_entity_id_as_string():
    uuid = uuid4()
    entity_id = EntityID(str(uuid))
    assert str(entity_id.id) == str(uuid)


def test_entity_id_invalid_id():
    with pytest.raises(Exception):
        entity_id = EntityID(1)

    with pytest.raises(Exception):
        entity_id = EntityID('test')

