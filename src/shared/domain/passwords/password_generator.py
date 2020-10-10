

from abc import ABC, abstractmethod


class PasswordGenerator(ABC):

    @abstractmethod
    def make(self, password):
        raise NotImplementedError("Not implemented yet")
