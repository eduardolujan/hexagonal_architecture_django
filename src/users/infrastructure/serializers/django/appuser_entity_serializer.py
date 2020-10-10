# -*- coding: utf-8 -*-


from src.shared.domain.serializers import EntitySerializer, EntitiesSerializer
from .django_user_serializer import AppUserSerializer


class AppUserEntitySerializer(EntitySerializer, EntitiesSerializer):
    def __init__(self, serializer_class=None):
        if not serializer_class:
            raise ValueError("Empty serializer_class")
        self.serializer_class = serializer_class

    def get_dto(self, data):
        app_user_serializer = self.serializer_class(data=data)
        is_valid_serializer = app_user_serializer.is_valid()
        if not is_valid_serializer:
            exception = Exception(f"Not valid data")
            exception.errors = app_user_serializer.errors
            raise exception

        serialized_data = app_user_serializer.data
        return serialized_data

    def get_entity(self, entity):
        app_user_serializer = AppUserSerializer(entity)
        serialized_data = app_user_serializer
        return serialized_data

    def get_dtos(self, data):
        app_user_serializer = AppUserSerializer(data=data, many=True)
        is_valid_serializer = app_user_serializer.is_valid()
        if not is_valid_serializer:
            exception = Exception(f"Not valid data")
            exception.errors = app_user_serializer.errors
            raise exception
        serializer_data = app_user_serializer.data
        return serializer_data

    def get_entities(self, entities):
        app_user_serializer = AppUserSerializer(entities, many=True)
        serializer_data = app_user_serializer.data
        return serializer_data

