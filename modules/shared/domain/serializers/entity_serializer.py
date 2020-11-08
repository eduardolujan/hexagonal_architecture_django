# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class EntitySerializer(ABC):
    @abstractmethod
    def get_dto_from_dict(self, data: dict):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def get_dto_from_entity(self, entity):
        raise NotImplementedError("Not implemented yet")

