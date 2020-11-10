# -*- coding: utf-8 -*-


from rest_framework import serializers


class DeleteUserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
