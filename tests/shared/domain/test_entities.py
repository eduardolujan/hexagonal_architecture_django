from uuid import uuid4

import pytest

from modules.shared.domain.value_objects import Uuid


def test_entity_id_as_string():
    _uuid = uuid4()
    entity_id = Uuid(str(_uuid))
    assert str(entity_id.value) == str(_uuid)


def test_entity_id_invalid_id():
    with pytest.raises(Exception):
        entity_id = Uuid(1)

    with pytest.raises(Exception):
        entity_id = Uuid('test')

