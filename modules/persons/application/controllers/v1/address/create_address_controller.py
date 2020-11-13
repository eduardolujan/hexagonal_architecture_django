# -*- coding: utf-8 -*-


# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Application
from modules.persons.application.create import AddressCreator
from modules.persons.application.create.command import CreateAddressCommand
# Domain
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers import SerializerManager
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.bus.message import MessageBus
from modules.persons.domain.repository import AddressRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class CreateAddressController:
    """
    CreateAddressController
    """

    def __init__(self,
                 request: Request,
                 response: Response,
                 address_serializer_manager: SerializerManager,
                 address_repository: AddressRepository,
                 unit_of_work: UnitOfWork,
                 message_bus=MessageBus):

        if not isinstance(address_repository, AddressRepository):
            raise ValueError(f"Parameter address_repository: {address_repository} "
                             f"is not instance of AddressRepository")

        if not isinstance(unit_of_work, UnitOfWork):
            raise ValueError(f"Paramter unit_of_work:{unit_of_work} "
                             f"is not instance of UnitOfWork")

        if not isinstance(message_bus, MessageBus):
            raise ValueError(f"Paramter unit_of_work:{message_bus} "
                             f"is not instance of MessageBus")

        # Http objects
        self.__request = request
        self.__response = response
        self.__serializer_manager = address_serializer_manager

        # Create  Address
        self.__repository = address_repository
        self.__unit_of_work = unit_of_work
        self.__bus = message_bus

    def __call__(self) -> Response:
        try:
            address_data = self.__request.get_body()

            create_address_command = CreateAddressCommand(
                id=address_data.get('id'),
                street=address_data.get('street'),
                interior_number=address_data.get('interior_number'),
                outside_number=address_data.get('outside_number'),
                zip_code=address_data.get('zip_code'),
                city=address_data.get('city'),
                borough=address_data.get('borough'),
                state=address_data.get('state'),
                country=address_data.get('country'))

            address_creator = AddressCreator(
                self.__repository,
                self.__unit_of_work,
                self.__bus)

            address_creator(create_address_command)

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
