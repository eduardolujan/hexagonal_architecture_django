


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
        """
        Constructor
        @param id:
        @type id:
        @param name:
        @type name:
        @param last_name:
        @type last_name:
        @param second_last_name:
        @type second_last_name:
        @param address:
        @type address:
        @param phone:
        @type phone:
        """
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__second_last_name = second_last_name
        self.__address = address
        self.__phone = phone

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def second_last_name(self):
        return self.__second_last_name

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone



