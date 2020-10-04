# -*- coding: utf-8 -*-


from src.shared.domain.serializers import EntitiesSerializer
from src.shared.domain.repository import AbstractRepository


class AppUsersSerializedService:
    def __init__(self, user_repository: AbstractRepository, entity_serializer: EntitiesSerializer):
        self.user_repository = user_repository
        self.entity_serializer = entity_serializer

    def all(self):
        users = self.user_repository.all()
        serialized_users = self.entity_serializer.get_entities(users)
        return serialized_users
