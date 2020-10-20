# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.infrastructure.requests.django import Request as DjangoRequest
from src.shared.infrastructure.responses.django import RestResponse as DjangoRestResponse
from src.shared.infrastructure.persistence.django import UnitOfWork as DjangoUnitOfWork
from src.shared.infrastructure.passwords.django import PasswordCreator as DjangoPasswordCreator
from src.users.infrastructure.repository.django import (
    UserRepository as DjangoUserRepository
)
from src.shared.infrastructure.serializers.django.serializer_manager import SerializerManager as DjangoSerializerManager
from src.users.infrastructure.serializers.django import (
    GetUserSerializer as DjangoGetUserSerializer,
    UserSerializer as DjangoUserSerializer
)
from src.users.application.api.v1 import UserGetApi, CreateUserApi


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, id):
        request = DjangoRequest(request)
        response = DjangoRestResponse()
        user_repository = DjangoUserRepository()
        request_serializer_manager = DjangoSerializerManager(DjangoGetUserSerializer)
        response_serializer_manager = DjangoSerializerManager(DjangoUserSerializer)
        user_get_api = UserGetApi(request,
                                  response,
                                  user_repository,
                                  request_serializer_manager,
                                  response_serializer_manager)
        response = user_get_api(id)
        return response

    def post(self, request):
        django_request = DjangoRequest(request)
        django_rest_response = DjangoRestResponse()
        django_user_repository = DjangoUserRepository()
        django_unit_of_work = DjangoUnitOfWork()
        django_password_creator = DjangoPasswordCreator()
        django_user_serializer_manager = DjangoSerializerManager(DjangoUserSerializer)
        create_user_api = CreateUserApi(django_request,
                                        django_rest_response,
                                        django_user_serializer_manager,
                                        django_user_repository,
                                        django_password_creator,
                                        django_unit_of_work)

        response = create_user_api()
        return response


