

from abc import ABC, abstractmethod


class GetController(ABC):
    """
    Get Controller
    """

    @abstractmethod
    def get(self):
        pass



