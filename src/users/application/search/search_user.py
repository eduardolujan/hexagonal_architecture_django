# -*- coding: utf-8 -*-


from uuid import UUID

from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService

from src.users.domain.repository import UserRepository
from src.users.domain.services import GetUser as GetUserService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class SearchUser:
    def __init__(self,
                 user_repository: UserRepository = None):
        """
        Get user service by id uuid v4
        @param user_repository:
        @param entity_serializer:
        """
        self.user_repository = user_repository

    def __call__(self, filters=None):
        if not filters:
            raise Exception('The values are empty try all instead')
        get_user_entity = GetUserService.get_user_by_id(id)
        user_entity = self.user_repository.get(get_user_entity)
        return user_entity




