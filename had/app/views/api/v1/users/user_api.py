# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService

from modules.shared.infrastructure.requests.django import Request
from modules.shared.infrastructure.responses.django import RestResponse
from modules.shared.infrastructure.persistence.django import UnitOfWork
from modules.shared.infrastructure.passwords.django import PasswordCreator

from modules.shared.infrastructure.serializers.django.serializer_manager import SerializerManager
from modules.shared.infrastructure.bus.event.in_memory_event_bus import EventBus
from modules.users.infrastructure.serializers.django import UserSerializer
from modules.users.infrastructure.serializers.django import GetUserSerializer
from modules.users.infrastructure.serializers.django import CreateUserSerializer
from modules.users.infrastructure.repository.django import UserRepository
# Application
from modules.users.application.controllers.v1 import UserFinderController
from modules.users.application.controllers.v1 import UserCreatorController
from modules.users.application.controllers.v1 import UserUpdaterController
from modules.users.application.controllers.v1 import UserDeleterController


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, _id: str = None):
        """
        Get User
        @param request:
        @type request:
        @param _id:
        @type _id:
        @return:
        @rtype:
        """
        request = Request(request)
        response = RestResponse()
        user_repository = UserRepository()
        request_serializer_manager = SerializerManager(GetUserSerializer)
        response_serializer_manager = SerializerManager(UserSerializer)

        user_finder_controller = UserFinderController(
            request,
            response,
            user_repository,
            request_serializer_manager,
            response_serializer_manager)
        response = user_finder_controller(_id)
        return response

    def post(self, request, _id: str = None):
        """
        Post User
        @param request: request
        @type request: response
        @param _id: user id
        @type _id: int
        @return: post response
        @rtype: Response
        """
        request = Request(request)
        response = RestResponse()
        user_repository = UserRepository()
        unit_of_work = UnitOfWork()
        password_creator = PasswordCreator()
        user_serializer_manager = SerializerManager(CreateUserSerializer)
        event_bus = EventBus()

        user_creator_controller = UserCreatorController(
            request,
            response,
            user_serializer_manager,
            user_repository,
            password_creator,
            unit_of_work,
            event_bus)
        response = user_creator_controller()
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
        request = Request(request)
        response = RestResponse()
        user_repository = UserRepository()
        unit_of_work = UnitOfWork()
        password_creator = PasswordCreator()
        user_serializer_manager = SerializerManager(CreateUserSerializer)

        user_updater_cotroller = UserUpdaterController(
            request,
            response,
            user_serializer_manager,
            user_repository,
            password_creator,
            unit_of_work)

        response = user_updater_cotroller()
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
        request = Request(request)
        response = RestResponse()
        user_repository = UserRepository()
        request_serializer_manager = SerializerManager(GetUserSerializer)
        user_deleter_controller = UserDeleterController(
            request,
            response,
            request_serializer_manager,
            user_repository)

        response = user_deleter_controller(_id)
        return response


