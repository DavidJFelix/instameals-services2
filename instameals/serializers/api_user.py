from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import APIUser


class APIUserSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = APIUser
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'last_login',
            'is_active',
            'modified',
            'created',
            'profile_image'
        )
