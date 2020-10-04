# -*- coding: utf-8 -*-


from src.shared.domain.serializers import EntitySerializer, EntitiesSerializer
from .django_user_serializer import AppUserSerializer


class AppUserEntitySerializer(EntitySerializer, EntitiesSerializer):

    def get_entity(self, entity):
        app_user_serializer = AppUserSerializer(entity)
        serializer_data = app_user_serializer.data
        return serializer_data

    def get_entities(self, entities):
        app_user_serializer = AppUserSerializer(entities, many=True)
        serializer_data = app_user_serializer.data
        return serializer_data
