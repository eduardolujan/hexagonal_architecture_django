# -*- coding: utf-8 -*-


from src.shared.domain.serializers import EntitiesSerializer
from src.users.domain.repository import UserRepository


class AllUser:
    def __init__(self, user_repository: UserRepository, entity_serializer: EntitiesSerializer):
        self.user_repository = user_repository
        self.entity_serializer = entity_serializer

    def all(self):
        users = self.user_repository.all()
        serialized_users = self.entity_serializer.get_entities(users)
        return serialized_users
