from rest_framework import serializers

from .models import (
    Address,
    Allergen,
    DietaryFilter,
    Image,
    Ingredient,
    APIUser,
    Location,
    Meal,
    Order,
    Review,
)


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id',)


class AllergenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergen
        fields = ('id', 'name')


class APIUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        fields = ('id',)
        extra_kwargs = {'password': {'write_only': True}}


class DietaryFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DietaryFilter
        fields = ('id', 'name')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('url',)


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id',)


class MealSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Meal
        fields = (
            'id',
            'name',
            'description',
            'allergens',
            'dietary_filters',
            'ingredients',
            'portions',
            'portions_available',
            'location',
            'available_from',
            'available_to',
            'seller',
            'preview_image',
            'images'
        )
        depth = 1


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id',)


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'rating')
