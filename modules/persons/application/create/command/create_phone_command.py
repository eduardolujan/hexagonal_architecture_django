from modules.shared.domain.bus.command import Command


class CreatePhoneCommand(Command):
    """
    CreatePersonCommand
    """

    def __init__(self,
                 id: str,
                 number: str,
                 extension: str):

        self.id = id
        self.number = number
        self.extension = extension

