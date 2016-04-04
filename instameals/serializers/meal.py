from rest_framework import serializers

from .api_user import APIUserSerializer
from ..models import Meal


class MealSerializer(serializers.HyperlinkedModelSerializer):
    seller = APIUserSerializer()

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
            'available_from',
            'available_to',
            'seller',
            'preview_image',
            'images'
        )
        depth = 1
