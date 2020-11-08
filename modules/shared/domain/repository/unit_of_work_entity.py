
from abc import ABC, abstractmethod


class UnitOfWorkEntityWrapper(ABC):
    """
    UnitOfWorkEntity interface
    """

    @abstractmethod
    def execute(self):
        """
        Execute
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")
