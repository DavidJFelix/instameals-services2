from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Ingredient


class IngredientSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Ingredient
        fields = (
            'id',
            'name',
        )
