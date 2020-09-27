
from abc import ABC, abstractmethod
from uuid import UUID
from dataclasses import dataclass


class EntityID:
    def __init__(self, id):
        self.id = UUID(id, version=4)
        pass

    def __deepcopy__(self, memodict={}):
        return str(self.id)

