from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import Ingredient


class IngredientSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
        )
