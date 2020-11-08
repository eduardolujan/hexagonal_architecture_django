# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers import SerializerManager
from modules.users.domain.repository import UserRepository
from modules.users.application.delete import UserDeleter as DeleteUserService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class DeleteUserApi:
    """
    Delete User API
    """
    def __init__(self,
                 request: Request,
                 response: Response,
                 request_serializer_manager: SerializerManager,
                 user_repository: UserRepository):

        # Http objects
        self.__request = request
        self.__response = response
        self.__request_serializer_manager = request_serializer_manager
        # Delete user
        self.__user_repository = user_repository

    def __call__(self, id: int) -> None:
        """
        Delete user by id
        @param id: user id
        @type id: int
        """
        try:
            delete_user_data = dict(id=id)
            delete_user_dto = self.__request_serializer_manager.get_dto_from_dict(delete_user_data)
            delete_user = DeleteUserService(self.__user_repository)
            delete_user(**delete_user_dto)
            response_data = dict(
                success=True,
                message='All ok',
            )
            return self.__response(response_data, status=http_status.HTTP_200_OK)

        except Exception as err:
            self.log.exception(f"Error in {__class__}::post, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            return self.__response(response_data, status=http_status.HTTP_400_BAD_REQUEST)
