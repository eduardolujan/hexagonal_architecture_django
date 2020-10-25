# -*- coding: utf-8 -*-

from rest_framework import status as http_status


from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.domain.requests import Request
from src.shared.domain.responses import Response
from src.shared.domain.repository import AbstractRepository
from src.users.application.get import GetUser as GetUserService
from src.shared.domain.serializers.serializer_manager import AbstractSerializerManager


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserGetApi:
    def __init__(self,
                 request: Request,
                 response: Response,
                 repository: AbstractRepository,
                 request_serializer_manager: AbstractSerializerManager,
                 response_serializer_manager: AbstractSerializerManager):
        self.request = request
        self.response = response
        self.repository = repository
        self.request_serializer_manager = request_serializer_manager
        self.response_serializer_manager = response_serializer_manager

    def __call__(self, id: str):
        try:
            get_user_data = dict(id=id)
            user_dto = self.request_serializer_manager.get_dto_from_dict(get_user_data)
            get_user_service = GetUserService(self.repository)
            user_entity = get_user_service(**user_dto)
            user_entity_serialized = self.response_serializer_manager.get_dto_from_entity(user_entity)
            response_data = dict(
                success=True,
                message='All ok',
                data=user_entity_serialized
            )
            response = self.response(response_data, status=http_status.HTTP_201_CREATED)
            return response

        except Exception as err:
            self.log.exception(f"Error in {__class__}::get, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            respose = self.response(response_data, status=http_status.HTTP_400_BAD_REQUEST)
            return respose
