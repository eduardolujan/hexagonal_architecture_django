# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from src.shared.infrastructure.persistence.django import UnitOfWork
from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.users.infrastructure.repository.django import UserRepository
from src.users.infrastructure.serializers.django import (
    DeleteUserSerializer as DjangoDeleteUserSerializer,
)
from src.users.application.delete import DeleteUser as DeleteUserService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class DeleteUserApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def delete(self, request, id):
        pass


