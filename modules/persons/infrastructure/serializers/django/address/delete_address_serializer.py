# -*- coding: utf-8 -*-


from rest_framework import serializers


class DeleteAddressSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=True)
