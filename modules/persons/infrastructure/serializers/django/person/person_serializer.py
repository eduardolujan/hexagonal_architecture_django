# -*- coding: utf-8 -*-


from rest_framework import serializers


class PersonSerializer(serializers.Serializer):
    """
    Person Serializer
    """
    id = serializers.UUIDField(required=True)
    name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    second_last_name = serializers.CharField(required=True)
    phone = serializers.UUIDField(required=True)
    address = serializers.UUIDField(required=True)


