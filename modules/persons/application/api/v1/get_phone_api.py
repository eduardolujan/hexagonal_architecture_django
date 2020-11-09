# -*- coding: utf-8 -*-


# Logs
from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService
# Shared
from modules.shared.domain.http import status as http_status
from modules.shared.domain.requests import Request
from modules.shared.domain.responses import Response
from modules.shared.domain.serializers.serializer_manager import SerializerManager
# Persons
from modules.persons.domain.repository import PhoneRepository
from modules.persons.application.get import PhoneGetter as PhoneGetterService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class GetPhoneApi:
    def __init__(self,
                 request: Request,
                 response: Response,
                 phone_repository: PhoneRepository,
                 request_serializer_manager: SerializerManager,
                 response_serializer_manager: SerializerManager):
        self.__request = request
        self.__response = response
        self.__repository = phone_repository
        self.__request_serializer_manager = request_serializer_manager
        self.__response_serializer_manager = response_serializer_manager

    def __call__(self, id: str):
        try:
            user_dto = self.request_serializer_manager.get_dto_from_dict(get_user_data)
            get_user_service = PhoneGetterService(self.repository)
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
