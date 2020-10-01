from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    batches = set()

    def __setattr__(self, key, value):
        if 'model' == key:
            raise ValueError("You are not allowed to change model instance")

    @abstractmethod
    def get(self, entity):
        pass

    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass

    @abstractmethod
    def search(self, entity):
        pass

    @abstractmethod
    def all(self):
        pass
