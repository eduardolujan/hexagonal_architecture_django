# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from modules.shared.infrastructure.serializers.django.serializer_manager import (
    SerializerManager as DjangoSerializerManager,
)
from modules.users.infrastructure.serializers.django import (
    UserSerializer as DjangoUserSerializer,
    GetUserSerializer as DjangoGetUserSerializer,
    CreateUserSerializer as DjangoCreateUserSerializer,
)
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.infrastructure.requests.django import Request as DjangoRequest
from modules.shared.infrastructure.responses.django import RestResponse as DjangoRestResponse
from modules.shared.infrastructure.persistence.django import UnitOfWork as DjangoUnitOfWork
from modules.shared.infrastructure.passwords.django import PasswordCreator as DjangoPasswordCreator
from modules.persons.infrastructure.repository.django import PersonRepository as DjangoPersonRepository
from modules.persons.application.controllers.v1.person import CreatePersonController, GetUserController


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, id: str = None):
        """
        Get User
        @param request:
        @type request:
        @param id:
        @type id:
        @return:
        @rtype:
        """
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        person_repository = DjangoPersonRepository()
        request_serializer_manager = DjangoSerializerManager(DjangoGetUserSerializer)
        response_serializer_manager = DjangoSerializerManager(DjangoUserSerializer)
        get_user_controller = GetUserController(
            request,
            response,
            person_repository,
            request_serializer_manager,
            response_serializer_manager)
        response = get_user_controller(id)
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
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        person_repository = DjangoPersonRepository()
        unit_of_work = DjangoUnitOfWork()
        password_creator = DjangoPasswordCreator()
        user_serializer_manager = DjangoSerializerManager(DjangoCreateUserSerializer)
        create_user_controller = CreatePersonController(
            request,
            response,
            user_serializer_manager,
            person_repository,
            password_creator,
            unit_of_work)
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


