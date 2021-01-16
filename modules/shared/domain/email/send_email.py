

from abc import ABC, abstractmethod
from typing import NoReturn, List


class EmailSender(ABC):
    """
    Send email
    """

    @abstractmethod
    def send_email(self, _from: str, to: List[str], message: str) -> NoReturn:
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

