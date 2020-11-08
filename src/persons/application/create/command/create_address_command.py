

from src.shared.domain.bus.command import Command


class CreateAddressCommand(Command):
    """
    CreatePersonCommand
    """

    def __init__(self,
                 id: str,
                 street: str,
                 interior_number: str,
                 outside_number: str,
                 zip_code: str,
                 city: str,
                 borough: str,
                 state: str,
                 country: str):

        self.__id = id
        self.__street = street
        self.__interior_number = interior_number
        self.__outside_number = outside_number
        self.__zip_code = zip_code
        self.__city = city
        self.__borough = borough
        self.__state = state
        self.__country = country

