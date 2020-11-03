from abc import ABC, abstractmethod


class SessionUnitOfWork(ABC):
    """
    Session Unit of Work
    """

    @abstractmethod
    def add(self, create_entity):
        raise NotImplementedError("Not implemented yet")
