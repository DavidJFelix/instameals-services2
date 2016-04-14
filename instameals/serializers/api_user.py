from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import APIUser


class APIUserSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = APIUser
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'profile_image'
        )
