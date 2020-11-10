# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class EntitiesSerializer(ABC):
    @abstractmethod
    def get_dtos_from_dicts(self, dicts):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def get_dtos_from_entities(self, entities):
        raise NotImplementedError("Not implemented yet")
