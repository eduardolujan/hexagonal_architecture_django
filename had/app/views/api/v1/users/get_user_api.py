# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from src.shared.infrastructure.logs import LoggerDecorator, PyLoggerService
from src.users.infrastructure.repository.django import UserRepository
from src.users.infrastructure.serializers.django import UserEntitySerializer
from src.users.application.get import GetUser as GetUserService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class GetUserApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, id):
        user_repository = UserRepository()
        entity_serializer = UserEntitySerializer()
        get_user_service = GetUserService(user_repository)
        user_entity = get_user_service(id)
        user_data = entity_serializer.get_dto_from_entity(user_entity)
        response_data = dict(
            success=True,
            message='All ok',
            data=user_data
        )
        return Response(response_data, status=status.HTTP_200_OK)


