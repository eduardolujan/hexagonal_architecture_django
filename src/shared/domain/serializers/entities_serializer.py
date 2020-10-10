# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class EntitiesSerializer(ABC):
    @abstractmethod
    def get_dtos(self, data):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def get_entities(self, data):
        raise NotImplementedError("Not implemented yet")
