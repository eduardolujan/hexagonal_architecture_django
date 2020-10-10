from abc import ABC, abstractmethod


from src.shared.domain.repository import AbstractRepository


class UserRepository(ABC):
    @abstractmethod
    def all(self):
        raise NotImplementedError("Not implemented error")

    @abstractmethod
    def create(self, entity):
        raise NotImplementedError("Not implemented error")

