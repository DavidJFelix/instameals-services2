from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Cusine


class CusineSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Cusine
        fields = (
            'id',
            'name',
            'description',
        )
