# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class EntitySerializer(ABC):
    @abstractmethod
    def get_entity(self, entity):
        raise NotImplementedError("Not implemented yet")


class EntitiesSerializer(ABC):
    @abstractmethod
    def get_entities(self, entities):
        raise NotImplementedError("Not implemented yet")
