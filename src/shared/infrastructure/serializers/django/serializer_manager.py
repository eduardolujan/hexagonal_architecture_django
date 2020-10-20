# -*- coding: utf-8 -*-


from src.shared.domain.serializers import SerializerManager as AbstractSerializerManager
from src.shared.infrastructure.log import LoggerDecorator, PyLoggerService


@LoggerDecorator(logger=PyLoggerService(file_path=__file__))
class SerializerManager(AbstractSerializerManager):

    def __init__(self, serializer):
        if not serializer:
            raise ValueError("You need to pass serializer")
        self.serializer = serializer

    def get_dto_from_dict(self, data):
        """
        Gets dict of the entity using user_serializer::DjangoUserSerializer
        @param data: data to serialize
        @return:
        """
        user_serializer = self.serializer(data=data)
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
        if entity is None:
            return None
        user_serializer = self.serializer(entity)
        serialized_data = user_serializer.data
        return serialized_data

    def get_dtos_from_dicts(self, data):
        """

        """
        user_serializer = self.serializer(data=data, many=True)
        is_valid_serializer = user_serializer.is_valid()
        if not is_valid_serializer:
            self.log.error(f"Serializer is not valid err:{user_serializer.errors}")
            exception = Exception(f"Not valid data")
            exception.errors = user_serializer.errors
            raise exception

        serializer_data = user_serializer.data
        return serializer_data

    def get_dtos_from_entities(self, entities):
        """

        """
        user_serializer = self.serializer(entities, many=True)
        serializer_data = user_serializer.data
        return serializer_data
