from abc import ABC, abstractmethod
from typing import List


class DomainEventSuscriber(ABC):
    """
    Domain Event Suscriber
    """

    def suscribed_to(self) -> List:
        """
        Suscribed to
        @return: List
        @rtype: List
        """
        raise NotImplementedError("Not implemented yet")
