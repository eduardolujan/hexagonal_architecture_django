# -*- coding: utf-8 -*-


from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=False, allow_blank=True)

