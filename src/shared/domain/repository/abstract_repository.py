from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    def __setattr__(self, key, value): ...



