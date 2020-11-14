# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


#Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.persons.infrastructure.repository.django import AddressRepository as DjangoAddressRepository
from modules.shared.infrastructure.bus.event import InMemoryEventBus
from modules.shared.infrastructure.requests.django import Request as DjangoRequest
from modules.shared.infrastructure.responses.django import RestResponse as DjangoRestResponse
from modules.shared.infrastructure.persistence.django import UnitOfWork as DjangoUnitOfWork
from modules.shared.infrastructure.passwords.django import PasswordCreator as DjangoPasswordCreator
from modules.persons.infrastructure.serializers.django.address import (
    AddressSerializer as DjangoAddressSerializer,
    GetAddressSerializer as DjangoGetAddressSerializer,
)
from modules.shared.infrastructure.serializers.django.serializer_manager import (
    SerializerManager as DjangoSerializerManager
)
# Application
from modules.persons.application.controllers.v1.person import PersonFinderController
from modules.persons.application.controllers.v1.person import PersonCreatorController


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class AddressApi(APIView):
    """
    Address API
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, id):
        """
        Get User
        @param request:
        @type request:
        @param _id:
        @type _id:
        @return:
        @rtype:
        """
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        address_repository = DjangoAddressRepository()
        request_serializer_manager = DjangoSerializerManager(DjangoGetAddressSerializer)
        response_serializer_manager = DjangoSerializerManager(DjangoAddressSerializer)
        in_memory_event_bus = InMemoryEventBus()

        person_finder_controller = PersonFinderController(
            request,
            response,
            address_repository,
            request_serializer_manager,
            response_serializer_manager,
            in_memory_event_bus)

        response = person_finder_controller(id)
        return response

    def post(self, request):
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        user_repository = DjangoAddressRepository()
        unit_of_work = DjangoUnitOfWork()
        address_serializer_manager = DjangoSerializerManager(DjangoAddressSerializer)
        in_memory_event_bus = InMemoryEventBus()

        create_user_controller = CreateAddressController(
            request,
            response,
            address_serializer_manager,
            user_repository,
            unit_of_work,
            in_memory_event_bus)
        response = create_user_controller()
        return response

    def put(self, request, _id: str = None):
        """
        Update User
        @param request: request
        @type request: response
        @param _id: user id
        @type _id: int
        @return: post response
        @rtype: Response
        """
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        user_repository = DjangoUserRepository()
        unit_of_work = DjangoUnitOfWork()
        password_creator = DjangoPasswordCreator()
        user_serializer_manager = DjangoSerializerManager(DjangoCreateUserSerializer)
        update_user_api = UpdateUserApi(request,
                                        response,
                                        user_serializer_manager,
                                        user_repository,
                                        password_creator,
                                        unit_of_work)
        response = update_user_api()
        return response

    def delete(self, request, _id):
        """
        Delete user api
        @param request:
        @type request:
        @param _id:
        @type _id:
        @return:
        @rtype:
        """
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        user_repository = DjangoUserRepository()
        request_serializer_manager = DjangoSerializerManager(DjangoGetUserSerializer)
        delete_user_api = DeleteUserApi(request,
                                        response,
                                        request_serializer_manager,
                                        user_repository)
        response = delete_user_api(_id)
        return response


