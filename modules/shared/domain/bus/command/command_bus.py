

from typing import NoReturn
from abc import ABC, abstractmethod
from .command import Command


class CommandBus(ABC):
    """
    Command bus
    """

    @abstractmethod
    def dispatch(self, command: Command) -> NoReturn:
        """
        Dispatch command
        @param command: command instance
        @type command: src.shared.co
        @return:
        @rtype:
        """
        raise NotImplementedError("Not implemented yet")

