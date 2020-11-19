

from abc import ABC, abstractmethod
from typing import NoReturn


class SendEmail(ABC):
    """
    Send email
    """

    @abstractmethod
    def send(self, _from: str, to: str, message: str) -> NoReturn:
        """
        Send email
        @param _from: from email
        @type _from: str
        @param to: to email
        @type to: str
        @param message: message
        @type message: str
        @return: No Return
        @rtype: NoReturn
        """
        raise NotImplementedError("Not implemented yet")
