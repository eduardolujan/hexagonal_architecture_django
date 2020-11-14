# -*- coding: utf-8 -*-


from rest_framework import status as http_status

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers import SerializerManager
from modules.users.domain.repository import UserRepository
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.passwords import PasswordGenerator
from modules.users.application.update import UserUpdater as UpdateUserService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UpdateUserController:
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
        """
        Update User Api
        @param request: request implementation
        @type request: src.shared.domain.requests.Request
        @param response: response implementation
        @type response: src.shared.domain.responses.Response
        @param serializer_manager:
        @type serializer_manager:
        @param user_repository:
        @type user_repository:
        @param password_generator:
        @type password_generator:
        @param unit_of_work:
        @type unit_of_work:
        """

        # Http objects
        self.__request = request
        self.__response = response
        self.__serializer_manager = serializer_manager
        # Create  user
        self.__user_repository = user_repository
        self.__password_generator = password_generator
        self.__unit_of_work = unit_of_work

    def __call__(self):
        try:
            user_data = self.__request.get_body()
            user_dto = self.__serializer_manager.get_dto_from_dict(user_data)
            update_user = UpdateUserService(self.__user_repository, self.__password_generator, self.__unit_of_work)
            update_user(**user_dto)
            response_data = dict(
                success=True,
                message='All ok',
            )
            return self.__response(response_data, status=http_status.HTTP_201_CREATED)

        except Exception as err:
            self.log.exception(f"Error in {__class__}::post, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            return self.__response(response_data, status=http_status.HTTP_400_BAD_REQUEST)
