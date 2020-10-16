# -*- coding: utf-8 -*-


from .django_user_serializer import UserSerializer as DjangoUserSerializer
from src.users.domain.entities import AppUser as UserEntity
from src.shared.domain.serializers import EntitySerializer, EntitiesSerializer
from src.shared.infrastructure.logs import LoggerDecorator, PyLoggerService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class UserEntitySerializer(EntitySerializer, EntitiesSerializer):
    user_serializer = DjangoUserSerializer

    def __init__(self):
        pass

    def get_dto(self, data):
        """
        Gets dict of the entity using user_serializer::DjangoUserSerializer
        @param data: data to serialize
        @return:
        """
        user_serializer = self.user_serializer(data=data)
        is_valid_serializer = user_serializer.is_valid()
        if not is_valid_serializer:
            self.log.error(f"Serializer is not valid err:{user_serializer.errors}")
            exception = Exception(f"Not valid data")
            exception.errors = user_serializer.errors
            raise exception

        serialized_data = user_serializer.data
        return serialized_data

    def get_dto_from_entity(self, entity):
        """
        Gets entity
        @param entity:
        @return:
        """
        user_serializer = self.user_serializer(entity)
        serialized_data = user_serializer.data
        return serialized_data

    def get_dtos(self, data):
        user_serializer = self.user_serializer(data=data, many=True)
        is_valid_serializer = user_serializer.is_valid()
        if not is_valid_serializer:
            self.log.error(f"Serializer is not valid err:{user_serializer.errors}")
            exception = Exception(f"Not valid data")
            exception.errors = user_serializer.errors
            raise exception
        serializer_data = user_serializer.data
        return serializer_data

    def get_dto_from_entities(self, entities):
        user_serializer = self.user_serializer(entities, many=True)
        serializer_data = user_serializer.data
        return serializer_data

