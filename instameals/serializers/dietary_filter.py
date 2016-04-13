from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import DietaryFilter


class DietaryFilterSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = DietaryFilter
        fields = (
            'id',
            'name',
        )
