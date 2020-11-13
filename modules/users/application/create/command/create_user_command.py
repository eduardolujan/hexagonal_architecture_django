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

    @property
    def id(self):
        """
        Getter of id
        @return: id
        @rtype: str
        """
        return self.__id

    @id.setter
    def id_setter(self, value):
        """
        Getter of id
        @return: id
        @rtype: str
        """
        raise Exception("Not allowed assign id directly")

    @property
    def username(self):
        """
        Getter of username
        @return: username
        @rtype: str
        """
        return self.__username

    @username.setter
    def username_setter(self, value):
        """
        Setter of username
        @return: id
        @rtype: str
        """
        raise Exception("Not allowed assign username directly")

    @property
    def password(self):
        """
        Getter of id
        @return: id
        @rtype: str
        """
        return self.__password

    @password.setter
    def password_setter(self, value):
        raise Exception("Not allowed assign password directly")


    @property
    def email(self):
        """
        Getter of email
        @return: email
        @rtype: str
        """
        return self.__email

    @email.setter
    def email_setter(self, value):
        raise Exception("Not allowed assign email directly")




