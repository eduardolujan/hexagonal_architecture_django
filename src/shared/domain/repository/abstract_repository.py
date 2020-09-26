
from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    batches = set()

    @abstractmethod
    def add(self, entity):
        pass

    @abstractmethod
    def edit(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def search(self, **fields):
        pass
