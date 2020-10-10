

from __future__ import annotations
from abc import ABC, abstractmethod

from src.shared.domain.repository import AbstractRepository


class AbstractUnitOfWork(ABC):

    def __enter__(self) -> AbstractUnitOfWork:
        """
        Magic method __enter__
        @return:
        """
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Magic method __exit__
        @param exc_type:
        @param exc_val:
        @param exc_tb:
        """
        self.rollback()

    @abstractmethod
    def commit(self):
        """
        Commit transaction
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def rollback(self):
        """
        Rollback transaction
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def add(self, entity):
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def flush(self):
        raise NotImplementedError("Not implemented yet")

    @property
    def session(self):
        class HelperClass:
            @classmethod
            def add(cls, entity):
                self.add(entity)
        return HelperClass
