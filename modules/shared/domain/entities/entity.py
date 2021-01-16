from modules.shared.domain.aggregate import AggregateRoot
from modules.shared.domain.value_objects import Uuid


class EntityId(AggregateRoot):
    """
    Entity ID
    """

    id = Uuid

