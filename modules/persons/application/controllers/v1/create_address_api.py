# -*- coding: utf-8 -*-


from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers import SerializerManager
from modules.users.domain.repository import UserRepository
from modules.shared.domain.repository import UnitOfWork
from modules.shared.domain.passwords import PasswordGenerator
from modules.persons.application.create import AddressCreator


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class CreateAddressApi:
    """
    CreateAddressApi
    """

    def __init__(self,
                 request: Request,
                 response: Response,
                 serializer_manager: SerializerManager,
                 user_repository: UserRepository,
                 password_generator: PasswordGenerator,
                 unit_of_work: UnitOfWork):

        # Http objects
        self.__request = request
        self.__response = response
        self.__serializer_manager = serializer_manager
        # Create  user
        self.___user_repository = user_repository
        self.__password_generator = password_generator
        self.__unit_of_work = unit_of_work

    def __call__(self) -> Response:
        """
        Create User API
        @return: Instance -> AbstractResponse
        @rtype: AbstractResponse implementation
        """
        try:
            user_data = self.__request.get_body()
            user_dto = self.__serializer_manager.get_dto_from_dict(user_data)
            create_user = AddressCreator(self.___user_repository, self.__password_generator, self.__unit_of_work)
            create_user(**user_dto)
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
