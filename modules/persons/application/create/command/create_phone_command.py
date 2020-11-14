from modules.shared.domain.bus.command import Command


class CreatePhoneCommand(Command):
    """
    CreatePersonCommand
    """

    def __init__(self,
                 id: str,
                 number: str,
                 extension: str):

        self.__id = id
        self.__number = number
        self.__extension = extension

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        raise Exception(f"You can't assign directly the id")

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        raise Exception(f"You can't assign directly the number")

    @property
    def extension(self):
        return self.__extension

    @extension.setter
    def extension(self, value):
        raise Exception(f"You can't assign directly the extension")

