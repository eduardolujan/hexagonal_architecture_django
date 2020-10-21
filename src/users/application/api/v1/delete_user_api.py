# -*- coding: utf-8 -*-


from rest_framework import status as http_status

from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.domain.requests import AbstractRequest
from src.shared.domain.responses import AbstractResponse
from src.shared.domain.serializers import AbstractSerializerManager
from src.users.domain.repository import UserRepository
from src.shared.domain.repository import AbstractUnitOfWork
from src.shared.domain.passwords import PasswordGenerator
from src.users.application.create import CreateUser


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UpdateUserApi:
    def __init__(self,
                 request: AbstractRequest,
                 response: AbstractResponse,
                 serializer_manager: AbstractSerializerManager,
                 user_repository: UserRepository,
                 password_generator: PasswordGenerator,
                 unit_of_work: AbstractUnitOfWork):

        # Http objects
        self.request = request
        self.response = response
        self.serializer_manager = serializer_manager
        # Create  user
        self.user_repository = user_repository
        self.password_generator = password_generator
        self.unit_of_work = unit_of_work

    def __call__(self):
        try:
            user_data = self.request.get_body()
            user_dto = self.serializer_manager.get_dto_from_dict(user_data)
            create_user = CreateUser(self.user_repository, self.password_generator, self.unit_of_work)
            create_user(**user_dto)
            response_data = dict(
                success=True,
                message='All ok',
            )
            return self.respose(response_data, status=http_status.HTTP_201_CREATED)

        except Exception as err:
            self.log.exception(f"Error in {__class__}::post, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            return self.respose(response_data, status=http_status.HTTP_400_BAD_REQUEST)
