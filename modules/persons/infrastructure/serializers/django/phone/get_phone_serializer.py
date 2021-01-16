# -*- coding: utf-8 -*-


from rest_framework import serializers


class GetPhoneSerializer(serializers.Serializer):
    """
    Get Address Serializer
    """
    id = serializers.UUIDField(required=True)
