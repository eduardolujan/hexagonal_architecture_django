# -*- coding: utf-8 -*-


# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Application
from modules.persons.application.create import PhoneCreator
from modules.persons.application.create.command import CreatePhoneCommand
# Domain
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers import SerializerManager
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.bus.event import EventBus
from modules.persons.domain.repository import PhoneRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class CreatePhoneController:
    """
    CreatePhoneController
    """

    def __init__(self,
                 request: Request,
                 response: Response,
                 address_serializer_manager: SerializerManager,
                 address_repository: PhoneRepository,
                 unit_of_work: UnitOfWork,
                 event_bus: EventBus):

        if not isinstance(address_repository, PhoneRepository):
            raise ValueError(f"Parameter address_repository: {address_repository} "
                             f"is not instance of PhoneRepository")

        if not isinstance(unit_of_work, UnitOfWork):
            raise ValueError(f"Paramter unit_of_work:{unit_of_work} "
                             f"is not instance of UnitOfWork")

        if not isinstance(event_bus, EventBus):
            raise ValueError(f"Parameter unit_of_work:{event_bus} "
                             f"is not instance of MessageBus")

        self.__request = request
        self.__response = response
        self.__serializer_manager = address_serializer_manager
        self.__repository = address_repository
        self.__unit_of_work = unit_of_work
        self.__event_bus = event_bus

    def __call__(self) -> Response:
        try:
            phone_data = self.__request.get_body()

            create_phone_command = CreatePhoneCommand(
                id=phone_data.get('id'),
                number=phone_data.get('number'),
                extension=phone_data.get('extension'))

            phone_creator = PhoneCreator(
                self.__repository,
                self.__unit_of_work,
                self.__event_bus)

            phone_creator(create_phone_command)

            response_data = dict(
                success=True,
                message='All ok',
            )
            return self.__response(response_data,
                                   status=http_status.HTTP_201_CREATED)

        except Exception as err:
            self.log.exception(f"Error in {__class__}::post, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            return self.__response(response_data,
                                   status=http_status.HTTP_400_BAD_REQUEST)
