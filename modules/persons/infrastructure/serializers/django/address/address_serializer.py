# -*- coding: utf-8 -*-


from rest_framework import serializers


class AddressSerializer(serializers.Serializer):
    """
    Address Serializer
    """
    id = serializers.UUIDField(required=True)
    street = serializers.CharField(required=True)
    interior_number = serializers.CharField(required=True)
    outside_number = serializers.CharField(required=True)
    zip_code = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    borough = serializers.CharField(required=True)
    state = serializers.CharField(required=False)
    country = serializers.CharField(required=False)


