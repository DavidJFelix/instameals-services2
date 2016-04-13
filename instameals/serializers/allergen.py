from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Allergen


class AllergenSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Allergen
        fields = (
            'id',
            'name',
            'description',
        )
