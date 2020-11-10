# -*- coding: utf-8 -*-


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.users.infrastructure.repository.django import UserRepository as DjangoUserRepository
from modules.shared.infrastructure.serializers.django import SerializerManager
from modules.users.infrastructure.serializers.django import UserSerializer as DjangoUserSerializer
from modules.users.application.all import AllUsers as AllUsersService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class ListUsersApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        user_repository = DjangoUserRepository()
        serializer_manager = SerializerManager(DjangoUserSerializer)
        all_users_service = AllUsersService(user_repository)
        user_entities = all_users_service.all()
        user_dtos = serializer_manager.get_dtos_from_entities(user_entities)
        response_data = dict(
            success=True,
            message='All ok',
            data=user_dtos
        )
        self.log.info('UserListApi::get, done')
        return Response(response_data, status=status.HTTP_200_OK)


