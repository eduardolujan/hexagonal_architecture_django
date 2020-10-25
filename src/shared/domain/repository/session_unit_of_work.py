from abc import ABC, abstractmethod


class SessionUnitOfWork(ABC):
    @abstractmethod
    def add(self, create_entity):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def update(self, update_entity):
        raise NotImplementedError("Not implemented yet")

