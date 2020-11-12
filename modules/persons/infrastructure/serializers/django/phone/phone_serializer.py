# -*- coding: utf-8 -*-


from rest_framework import serializers


class PhoneSerializer(serializers.Serializer):
    """
    Address Serializer
    """
    id = serializers.UUIDField(required=True)
    number = serializers.CharField(required=True)
    extension = serializers.CharField(required=True)


