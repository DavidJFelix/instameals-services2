from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Cuisine


class CuisineSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Cuisine
        fields = (
            'id',
            'name',
            'description',
        )
