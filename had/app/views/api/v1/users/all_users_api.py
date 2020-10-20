# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.users.infrastructure.repository.django import UserRepository
from src.users.infrastructure.serializers.django import UserEntitySerializer
from src.users.application.all import AllUsers as AllUsersService

@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class ListUsersApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        user_repository = UserRepository()
        entity_serializer = UserEntitySerializer()
        all_users_service = AllUsersService(user_repository, entity_serializer)
        user_entities = all_users_service.all()
        response_data = dict(
            success=True,
            message='All ok',
            data=user_entities
        )
        self.log.info('UserListApi::get, done')
        return Response(response_data, status=status.HTTP_200_OK)


