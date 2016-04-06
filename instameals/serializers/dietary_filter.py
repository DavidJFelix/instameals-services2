from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import DietaryFilter


class DietaryFilterSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DietaryFilter
        fields = (
            'id',
            'name',
        )
