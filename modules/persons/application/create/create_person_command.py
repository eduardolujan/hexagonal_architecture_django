
from typing import Optional
from modules.shared.domain.bus.command import Command


class CreatePersonCommand(Command):
    """
    CreatePersonCommand
    """

    def __init__(self,
                 id: str,
                 name: str,
                 last_name: str,
                 second_last_name: str,
                 address: Optional[str],
                 phone: Optional[str]):

        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__second_last_name = second_last_name
        self.__address = address
        self.__phone: str

