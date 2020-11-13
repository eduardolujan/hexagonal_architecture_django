# -*- coding: utf-8 -*-

# from __future__ import annotations
from typing import Optional, TypeVar
from abc import ABC, abstractmethod


UnitOfWork = TypeVar('UnitOfWork', bound='UnitOfWork')


class UnitOfWork(ABC):
    """
    Unit of work
    """

    @abstractmethod
    def commit(self):
        """
        Commit transaction
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def add(self, entity) -> None:
        """
        Add entity to transactions
        @param entity:
        @type entity:
        @return: None
        """
        raise NotImplementedError("Not implemented yet")

    @abstractmethod
    def flush(self) -> None:
        """
        Remove all transactions
        @return: None
        """
        raise NotImplementedError("Not implemented yet")
