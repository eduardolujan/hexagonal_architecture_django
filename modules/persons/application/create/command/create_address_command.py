# -*- coding: utf-8 -*-


from modules.shared.domain.bus.command import Command


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

    @property
    def id(self):
        """
        ID
        @return:
        @rtype:
        """
        return self.__id

    @property
    def street(self):
        """
        Street
        @return:
        @rtype:
        """
        return self.__street

    @property
    def interior_number(self):
        """

        @return:
        @rtype:
        """
        return self.__interior_number

    @property
    def outside_number(self):
        """

        @return:
        @rtype:
        """
        return self.__outside_number

    @property
    def zip_code(self):
        """

        @return:
        @rtype:
        """
        return self.__zip_code

    @property
    def city(self):
        """

        @return:
        @rtype:
        """
        return self.__city

    @property
    def borough(self):
        """

        @return:
        @rtype:
        """
        return self.__borough

    @property
    def state(self):
        """

        @return:
        @rtype:
        """
        return self.__state

    @property
    def country(self):
        """

        @return:
        @rtype:
        """
        return self.__country
