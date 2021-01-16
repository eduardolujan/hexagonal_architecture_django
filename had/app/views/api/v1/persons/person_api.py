# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.infrastructure.bus.event import InMemoryEventBus
from modules.shared.infrastructure.requests.django import Request as DjangoRequest
from modules.shared.infrastructure.responses.django import RestResponse
from modules.shared.infrastructure.persistence.django import UnitOfWork
from modules.persons.infrastructure.repository.django import PersonRepository
from modules.persons.infrastructure.serializers.django.person import PersonSerializer
from modules.persons.infrastructure.serializers.django.person import GetPersonSerializer
from modules.shared.infrastructure.serializers.django.serializer_manager import SerializerManager
# Application
from modules.persons.application.controllers.v1.person import PersonFinderController
from modules.persons.application.controllers.v1.person import PersonCreatorController


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class PersonApi(APIView):
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
        response = RestResponse()
        address_repository = PersonRepository()
        request_serializer_manager = SerializerManager(GetPersonSerializer)
        response_serializer_manager = SerializerManager(PersonSerializer)

        person_finder_controller = PersonFinderController(
            request,
            response,
            address_repository,
            request_serializer_manager,
            response_serializer_manager)

        response = person_finder_controller(id)
        return response

    def post(self, request):
        request = DjangoRequest(request)
        response = RestResponse()
        person_repository = PersonRepository()
        unit_of_work = UnitOfWork()
        person_serializer_manager = SerializerManager(PersonSerializer)
        in_memory_event_bus = InMemoryEventBus()

        person_creator_controller = PersonCreatorController(
            request,
            response,
            person_serializer_manager,
            person_repository,
            unit_of_work,
            in_memory_event_bus)

        response = person_creator_controller()
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


