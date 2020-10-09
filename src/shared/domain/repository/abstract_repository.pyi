from abc import ABC, abstractmethod
from typing import Set

class AbstractRepository(ABC):

    def __setattr__(self, key, value):
        if 'model' == key:
            raise ValueError("You are not allowed to change model instance")

    @abstractmethod
    def get(self, entity):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def create(self, entity):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def delete(self, entity):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def search(self, entity):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def all(self):
        raise NotImplementedError("Not implemented yet")
