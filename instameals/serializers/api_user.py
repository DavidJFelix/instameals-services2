from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import APIUser


class APIUserSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        fields = (
            'id',
            'username',
        )
