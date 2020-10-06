from abc import ABC, abstractmethod


class UserRepository(ABC):
    @abstractmethod
    def all(self):
        raise NotImplementedError("Not implemented error")

