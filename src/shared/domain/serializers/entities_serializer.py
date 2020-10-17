# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class EntitiesSerializer(ABC):
    @abstractmethod
    def get_dtos(self, data):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def get_dto_from_entities(self, data):
        raise NotImplementedError("Not implemented yet")
