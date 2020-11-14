# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Application
from modules.persons.application.get import AddressFinder
from modules.persons.application.get.query.address import AddressGetterQuery
# Domain
from modules.shared.domain.bus.message import MessageBus
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers.serializer_manager import SerializerManager
from modules.persons.domain.repository import AddressRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class GetAddressController:
    """
    User GET API
    """
    def __init__(self,
                 request: Request,
                 response: Response,
                 address_repository: AddressRepository,
                 request_serializer_manager: SerializerManager,
                 response_serializer_manager: SerializerManager,
                 message_bus: MessageBus):

        if not isinstance(address_repository, (AddressRepository,)):
            raise ValueError(f"Parameter address_repository:{address_repository} is not instance AddressRepository")

        if not isinstance(message_bus, MessageBus):
            raise ValueError(f"Parameter message_bus:{message_bus} is not instance MessageBus")

        self.__request = request
        self.__response = response
        self.__repository = address_repository
        self.__request_serializer_manager = request_serializer_manager
        self.__response_serializer_manager = response_serializer_manager
        self.__bus = message_bus

    def __call__(self, id: str):
        """
        Get Uset API
        @param id: User ID
        @type id: int
        @return: Response
        @rtype: Response
        """
        try:
            address_getter_query = AddressGetterQuery(id=id)
            get_address_getter = AddressFinder(self.__repository)
            user_entity = get_address_getter(address_getter_query)
            user_entity_serialized = self.__response_serializer_manager.get_dto_from_entity(user_entity)
            response_data = dict(
                success=True,
                message='All ok',
                data=user_entity_serialized
            )
            response = self.__response(response_data, status=http_status.HTTP_201_CREATED)
            return response

        except Exception as err:
            self.log.exception(f"Error in {__class__}::get, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            respose = self.__response(response_data, status=http_status.HTTP_400_BAD_REQUEST)
            return respose
