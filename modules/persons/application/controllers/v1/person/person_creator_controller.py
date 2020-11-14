# -*- coding: utf-8 -*-


# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Application
from modules.persons.application.create import PersonCreator
from modules.persons.application.create.command import CreatePersonCommand
# Domain
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers import SerializerManager
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.bus.event import EventBus
from modules.shared.domain.passwords import PasswordGenerator
from modules.persons.domain.repository import PersonRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PersonCreatorController:
    """
    CreateUserApi
    """

    def __init__(self,
                 request: Request,
                 response: Response,
                 serializer_manager: SerializerManager,
                 person_repository: PersonRepository,
                 unit_of_work: UnitOfWork,
                 event_bus: EventBus):

        # Http objects
        self.__request = request
        self.__response = response
        self.__serializer_manager = serializer_manager

        # Create  Person
        self.__person_repository = person_repository
        self.__unit_of_work = unit_of_work
        self.__event_bus = event_bus

    def __call__(self) -> Response:
        """
        Create Person API
        @return: Instance of Response
        @rtype: AbstractResponse implementation
        """
        try:
            person_data = self.__request.get_body()
            create_person_command = CreatePersonCommand(
                id=person_data.get('id'),
                name=person_data.get('name'),
                last_name=person_data.get('last_name'),
                second_last_name=person_data.get('second_last_name'),
                phone=person_data.get('phone'),
                address=person_data.get('address'),
            )
            person_creator = PersonCreator(self.__person_repository,
                                        self.__unit_of_work,
                                        self.__event_bus)

            person_creator(create_person_command)
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
