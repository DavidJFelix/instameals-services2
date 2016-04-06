import uuid

from rest_framework import serializers


class UUIDModelSerializerMixin(serializers.ModelSerializer):
    id = serializers.UUIDField(default=uuid.uuid4, read_only=True)