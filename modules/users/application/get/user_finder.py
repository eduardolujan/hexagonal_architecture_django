# -*- coding: utf-8 -*-


from typing import NoReturn

from modules.shared.infrastructure.log import LoggerDecorator, PyLoggerService

# Application
from modules.users.application.get.query import UserFinderQuery

# Domain
from modules.shared.domain.bus.query.query import Query
from modules.users.domain.entities import User as UserEntity
from modules.users.domain.repository import UserRepository
from modules.users.domain.services import UserFinderService
from modules.users.domain.value_objects import UserId


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserFinder:
    """
    User getter service
    """

    def __init__(self, user_repository: UserRepository):
        """
        Get user service by id uuid v4
        @param user_repository: user repository
        @param user_repository: UserRepository
        """
        if not isinstance(user_repository, UserRepository):
            raise NotImplementedError(f"Parameter user_repository: {user_repository} "
                                      f"is not instance of UserRepository")

        self.__repository = user_repository

    def __call__(self, user_finder_query: Query) -> UserEntity:
        user_id = UserId(user_finder_query.id)
        user_getter_entity = UserFinderService.get_user_entity(user_id)
        user_entity = self.__repository.get(user_getter_entity)
        return user_entity




