# -*- coding: utf-8 -*-


from modules.shared.domain.bus.command import Command


class CreateUserCommand(Command):
    """
    Create User Command
    """
    def __init__(self,
                 id: str,
                 username: str,
                 password: str,
                 email: str):
        """
        Create User Command
        @param id: id
        @type id: str
        @param username: username
        @type username: str
        @param password: password
        @type password: str
        @param email: email
        @type email: str
        """

        self.__id = id
        self.__username = username
        self.__password = password
        self.__email = email

