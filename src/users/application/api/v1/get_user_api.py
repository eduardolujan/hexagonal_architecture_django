# -*- coding: utf-8 -*-

from rest_framework import status as http_status


from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.domain.requests import AbstractRequest
from src.shared.domain.responses import AbstractResponse
from src.shared.domain.repository import AbstractRepository
from src.users.application.get import GetUser as GetUserService
from src.shared.domain.serializers.serializer_manager import AbstractSerializerManager


@LoggerDecorator(logger=PyLoggerService(file_path=__name__))
class UserGetApi:
    def __init__(self,
                 request: AbstractRequest,
                 response: AbstractResponse,
                 repository: AbstractRepository,
                 serializer_manager: AbstractSerializerManager):
        self.request = request
        self.response = response
        self.repository = repository
        self.serializer_manager = serializer_manager

    def __call__(self, id: str):
        try:
            get_user_data = dict(id=id)
            user_dto = self.serializer_manager.get_dto(get_user_data)
            get_user_service = GetUserService(self.repository)
            get_user_service(**user_dto)
            response_data = dict(
                success=True,
                message='All ok',
            )
            self.request(response_data, status=http_status.HTTP_201_CREATED)

        except Exception as err:
            self.log.exception(f"Error in {__class__}::get, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)
            return self.request(response_data, status=http_status.HTTP_400_BAD_REQUEST)
