# -*- coding: utf-8 -*-


from rest_framework import status as http_status

from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from src.shared.domain.requests import Request
from src.shared.domain.responses import Response
from src.shared.domain.serializers import SerializerManager
from src.users.domain.repository import UserRepository
from src.shared.domain.repository import UnitOfWork
from src.shared.domain.passwords import PasswordGenerator
from src.users.application.update import UpdateUser as UpdateUserService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UpdateUserApi:
    """
    Update User Api
    """
    def __init__(self,
                 request: Request,
                 response: Response,
                 serializer_manager: SerializerManager,
                 user_repository: UserRepository,
                 password_generator: PasswordGenerator,
                 unit_of_work: UnitOfWork):

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
            update_user = UpdateUserService(self.user_repository, self.password_generator, self.unit_of_work)
            update_user(**user_dto)
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
