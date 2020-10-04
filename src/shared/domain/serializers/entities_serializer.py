# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class EntitiesSerializer(ABC):
    @abstractmethod
    def get_entities(self, entities):
        raise NotImplementedError("Not implemented yet")
