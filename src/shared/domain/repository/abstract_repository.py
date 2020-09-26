
from abc import ABC, abstractmethod


class AbstractRepository(ABC):
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
    def search(self, entity):
        pass
