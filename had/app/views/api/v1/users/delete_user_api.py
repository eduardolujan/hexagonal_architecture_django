# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from src.shared.infrastructure.persistence.django import DjangoUnitOfWork
from src.shared.infrastructure.passwords import DjangoPasswordCreator
from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.users.infrastructure.repository.django import UserRepository
from src.users.infrastructure.serializers.django import (
    UserEntitySerializer,
)
from src.users.application.delete import DeleteUser as DeleteUserService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class CreateUserApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, id):
        try:
            delete_user_data = dict(id=id)
            user_entity_serializer = UserEntitySerializer()
            delete_user_dto = user_entity_serializer.get_dto(delete_user_data)
            user_repository = UserRepository()
            delete_user = DeleteUserService(user_repository)
            delete_user(**delete_user_dto)
            response_data = dict(
                success=True,
                message='All ok',
            )
            return Response(response_data, status=status.HTTP_201_CREATED)
        except Exception as err:
            self.log.exception(f"Error in {__class__}::post, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)


