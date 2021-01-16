

from modules.persons.application.create.command import CreatePersonCommand
from modules.users.domain.repository import UserRepository
from modules.shared.domain.email import EmailSender
from modules.users.domain.entities import UserId

class CreatePersonCommandHandler:
    """
    Create Person Command Handler
    """

    def __init__(self,
                 user_repository: UserRepository,
                 email_sender: EmailSender):

        self.__user_repository = user_repository
        self.__email_sender = email_sender

    def __call__(self, create_person_command: CreatePersonCommand):
        if type(create_person_command) is not CreatePersonCommand:
            raise Exception(f"Error command is invalid {CreatePersonCommand}")

        self.__user_repository.get()
