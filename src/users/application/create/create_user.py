

from src.shared.infrastructure.logs import LoggerDecorator, PyLoggerService
from src.shared.domain.repository import AbstractUnitOfWork
from src.shared.domain.passwords import PasswordGenerator
from src.users.domain.services import CreateUser as DomainCreateUser
from src.users.domain.repository import UserRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class CreateUser:
    def __init__(self,
                 user_repository: UserRepository,
                 password_generator: PasswordGenerator,
                 unit_of_work: AbstractUnitOfWork):
        """
        Create User contructor
        @param user_repository: User repository instance
        @param password_generator: Password generator instance
        @param unit_of_work: AbstractUnitOfWork
        """
        self.repository = user_repository
        self.password_generator = password_generator
        self.unit_of_work = unit_of_work

    def __call__(self, id: str=None, username: str=None, password: str=None, email: str=None, **fields):
        user_entity = DomainCreateUser.create_base_user(id, username, password, email, self.password_generator)
        with self.unit_of_work as uow:
            user = self.repository.create(user_entity)
            uow.session.add(user)
            uow.commit()


