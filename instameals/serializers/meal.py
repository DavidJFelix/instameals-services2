from rest_framework import serializers

from .address import AddressSerializer
from .allergen import AllergenSerializer
from .api_user import APIUserSerializer
from .dietary_filter import DietaryFilterSerializer
from .image import ImageSerializer
from .ingredient import IngredientSerializer
from .price import PriceSerializer
from .uuid import UUIDModelSerializerMixin
from ..models import Meal


class MealSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    allergens = AllergenSerializer(many=True)
    dietary_filters = DietaryFilterSerializer(many=True)
    ingredients = IngredientSerializer(many=True)
    pickup_address = AddressSerializer()
    price = PriceSerializer()
    seller = APIUserSerializer()
    preview_image = IngredientSerializer()
    images = ImageSerializer(many=True)

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
        depth = 1
