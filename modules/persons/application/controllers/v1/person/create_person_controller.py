# -*- coding: utf-8 -*-


# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Application
from modules.persons.application.create import PersonCreator
# Domain
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers import SerializerManager
from modules.users.domain.repository import UserRepository
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.bus.event import EventBus
from modules.shared.domain.passwords import PasswordGenerator



@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class CreatePersonController:
    """
    CreateUserApi
    """

    def __init__(self,
                 request: Request,
                 response: Response,
                 serializer_manager: SerializerManager,
                 user_repository: UserRepository,
                 password_generator: PasswordGenerator,
                 unit_of_work: UnitOfWork,
                 event_bus: EventBus):

        # Http objects
        self.__request = request
        self.__response = response
        self.__serializer_manager = serializer_manager
        # Create  user
        self.___user_repository = user_repository
        self.__password_generator = password_generator
        self.__unit_of_work = unit_of_work
        self.__event_bus = event_bus

    def __call__(self) -> Response:
        """
        Create User API
        @return: Instance -> AbstractResponse
        @rtype: AbstractResponse implementation
        """
        try:
            user_data = self.__request.get_body()
            user_dto = self.__serializer_manager.get_dto_from_dict(user_data)
            create_user = PersonCreator(self.___user_repository,
                                        self.__unit_of_work,
                                        self.__event_bus)
            create_user(**user_dto)
            response_data = dict(
                success=True,
                message='All ok',
            )
            return self.__response(response_data, status=http_status.HTTP_201_CREATED)

        except Exception as err:
            self.log.exception(f"Error in {__class__}::post, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            return self.__response(response_data, status=http_status.HTTP_400_BAD_REQUEST)
