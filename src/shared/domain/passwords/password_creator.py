

from abc import ABC, abstractmethod


class PasswordGenerator(ABC):

    @abstractmethod
    def create(self, password):
        raise NotImplementedError("Not implemented yet")
