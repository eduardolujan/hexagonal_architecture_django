# -*- coding: utf-8 -*-


from modules.shared.domain.bus.command import Command


class GetUserCommand(Command):
    """
    Create User Command
    """
    def __init__(self,
                 id: str):
        """
        Create User Command
        @param id: id
        @type id: str
        """

        self.__id = id

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
        raise Exception("Not allowed assign directly")




