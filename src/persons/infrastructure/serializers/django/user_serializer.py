# -*- coding: utf-8 -*-


from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=False, allow_blank=True)


class GetUserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)


class CreateUserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True)


