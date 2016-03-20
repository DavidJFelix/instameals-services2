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
    MealReview,
    Order,
    OrderReview,
    Review,
    SellerReview,
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
        fields = ('id', 'username',)


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


class MealReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MealReview
        fields = ('id',)


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id',)


class OrderReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderReview
        fields = ('id',)


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'rating')


class SellerReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SellerReview
        fields = ('id',)
