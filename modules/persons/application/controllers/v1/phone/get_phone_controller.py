# -*- coding: utf-8 -*-


# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Application
from modules.persons.application.get import PhoneGetter
from modules.persons.application.get.query.phone import PhoneGetterQuery
# Domain
from modules.shared.domain.bus.message import MessageBus
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers.serializer_manager import SerializerManager
from modules.persons.domain.repository import PhoneRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class GetPhoneController:
    """
    Get Phone Controller
    """

    def __init__(self,
                 request: Request,
                 response: Response,
                 phone_repository: PhoneRepository,
                 request_serializer_manager: SerializerManager,
                 response_serializer_manager: SerializerManager,
                 message_bus: MessageBus):

        if not isinstance(phone_repository, PhoneRepository):
            raise ValueError(f"Parameter phone_repository: {phone_repository} "
                             f"is not instance of PhoneRepository")

        if not isinstance(message_bus, MessageBus):
            raise ValueError(f"Parameter message_bus: {message_bus} "
                             f"is not instance of MessageBus")

        self.__request = request
        self.__response = response
        self.__repository = phone_repository
        self.__request_serializer_manager = request_serializer_manager
        self.__response_serializer_manager = response_serializer_manager
        self.__bus = message_bus

    def __call__(self, id: str):
        try:
            phone_getter_query = PhoneGetterQuery(id=id)
            phone_getter = PhoneGetter(self.__repository)
            phone_entity = phone_getter(phone_getter_query)
            phone_entity_serialized = self.response_serializer_manager.get_dto_from_entity(phone_entity)
            response_data = dict(
                success=True,
                message='All ok',
                data=phone_entity_serialized
            )
            response = self.response(response_data,
                                     status=http_status.HTTP_201_CREATED)

            return response

        except Exception as err:
            self.log.exception(f"Error in {__class__}::get, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            respose = self.response(response_data,
                                    status=http_status.HTTP_400_BAD_REQUEST)
            return respose
