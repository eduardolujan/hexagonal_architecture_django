# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod


class EntitySerializer(ABC):
    @abstractmethod
    def get_entity(self, en):
        raise NotImplementedError("Not implemented yet")
