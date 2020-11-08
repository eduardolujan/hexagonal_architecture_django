# -*- coding: utf-8 -*-


from rest_framework import serializers


class GetUserSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
