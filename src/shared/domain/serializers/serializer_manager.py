from abc import ABC

from .entity_serializer import EntitySerializer
from .entities_serializer import EntitiesSerializer


class AbstractSerializerManager(EntitySerializer, EntitiesSerializer, ABC):
    pass
