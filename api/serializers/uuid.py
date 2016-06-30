import uuid

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UUIDModelSerializerMixin(ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)
