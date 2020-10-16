from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def create(self, entity):
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def get(self, entity):
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def delete(self, entity):
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def all(self):
        raise NotImplementedError("Not implemented error")

