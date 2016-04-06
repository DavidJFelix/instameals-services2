from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import Allergen


class AllergenSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergen
        fields = (
            'id',
            'name',
            'description',
        )
