# -*- coding: utf-8 -*-

# Infra
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Application
from modules.users.application.get import UserFinder
from modules.users.application.get.query import UserGetterQuery
# Domain
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers.serializer_manager import SerializerManager
from modules.users.domain.repository import UserRepository


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserFinderController:
    """
    User GET API
    """

    def __init__(self,
                 request: Request,
                 response: Response,
                 user_repository: UserRepository,
                 request_serializer_manager: SerializerManager,
                 response_serializer_manager: SerializerManager):

        self.__request = request
        self.__response = response
        self.__repository = user_repository
        self.__request_serializer_manager = request_serializer_manager
        self.__response_serializer_manager = response_serializer_manager

    def __call__(self, id: str):
        """
        Get Uset API
        @param id: User ID
        @type id: int
        @return: Response
        @rtype: Response
        """
        try:
            user_getter_query = UserGetterQuery(id=id)
            get_user_service = UserFinder(self.__repository)
            user_entity = get_user_service(user_getter_query)
            user_entity_serialized = self.__response_serializer_manager.get_dto_from_entity(user_entity)
            response_data = dict(
                success=True,
                message='All ok',
                data=user_entity_serialized
            )
            response = self.__response(response_data, status=http_status.HTTP_200_OK)
            return response

        except Exception as err:
            self.log.exception(f"Error in {__class__}::get, err:{err}")
            response_data = dict(
                success=False,
                message=f"{err}"
            )
            if hasattr(err, 'errors'):
                response_data.update(errors=err.errors)

            respose = self.__response(response_data, status=http_status.HTTP_400_BAD_REQUEST)
            return respose
