from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Meal


class MealSerializer(UUIDModelSerializerMixin, ModelSerializer):
    """A meal serializer used for Create/Update CRUD/REST operations"""

    class Meta:
        model = Meal
        fields = (
            'id',
            'name',
            'description',
            'allergens',
            'dietary_filters',
            'ingredients',
            'pickup_address',
            'portions',
            'portions_available',
            'price',
            'available_from',
            'available_to',
            'seller',
            'preview_image',
            'images'
        )
