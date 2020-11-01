# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from src.shared.infrastructure.serializers.django.serializer_manager import (
    SerializerManager as DjangoSerializerManager,
)
from src.users.infrastructure.serializers.django import (
    UserSerializer as DjangoUserSerializer,
    GetUserSerializer as DjangoGetUserSerializer,
    CreateUserSerializer as DjangoCreateUserSerializer,
)
from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.infrastructure.requests.django import Request as DjangoRequest
from src.shared.infrastructure.responses.django import RestResponse as DjangoRestResponse
from src.shared.infrastructure.persistence.django import UnitOfWork as DjangoUnitOfWork
from src.shared.infrastructure.passwords.django import PasswordCreator as DjangoPasswordCreator
from src.users.infrastructure.repository.django import (
    UserRepository as DjangoUserRepository
)
from src.users.application.api.v1 import GetUserApi, CreateUserApi, UpdateUserApi, DeleteUserApi


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, _id: str = None):
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        user_repository = DjangoUserRepository()
        request_serializer_manager = DjangoSerializerManager(DjangoGetUserSerializer)
        response_serializer_manager = DjangoSerializerManager(DjangoUserSerializer)
        user_get_api = GetUserApi(request,
                                  response,
                                  user_repository,
                                  request_serializer_manager,
                                  response_serializer_manager)
        response = user_get_api(_id)
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
        user_repository = DjangoUserRepository()
        unit_of_work = DjangoUnitOfWork()
        password_creator = DjangoPasswordCreator()
        user_serializer_manager = DjangoSerializerManager(DjangoCreateUserSerializer)
        create_user_api = CreateUserApi(request,
                                        response,
                                        user_serializer_manager,
                                        user_repository,
                                        password_creator,
                                        unit_of_work)
        response = create_user_api()
        return response

    def update(self, request, _id: str = None):
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


