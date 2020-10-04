# -*- coding: utf-8 -*-


from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from drf_yasg.utils import swagger_auto_schema

from src.shared.infrastructure.logs import get_logger, cls_logger_decorator
from src.users.infrastructure.repository import AppUserRepository
from src.users.infrastructure.serializers.django import AppUserEntitySerializer
from src.users.application import AppUsersSerializedService

log = get_logger(__file__)


@cls_logger_decorator(file_name=__file__)
class UserListApi(APIView):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        user_repository = AppUserRepository()
        user_entity_serializer = AppUserEntitySerializer()
        user_serialized_service = AppUsersSerializedService(user_repository, user_entity_serializer)
        serialized_users = user_serialized_service.all()
        response_data = dict(
            success=True,
            message='All ok',
            data=serialized_users
        )
        self.log.info('Called')
        return Response(response_data, status=status.HTTP_200_OK)


