# Create your views here.
from rest_framework import mixins, viewsets

from .models import (
    Address,
    Allergen,
    APIUser,
    DietaryFilter,
    Image,
    Ingredient,
    Location,
    Meal,
    MealReview,
    Order,
    OrderReview,
    Review,
    SellerReview,
)
from .serializers import (
    AddressSerializer,
    AllergenSerializer,
    APIUserSerializer,
    DietaryFilterSerializer,
    ImageSerializer,
    IngredientSerializer,
    LocationSerializer,
    MealSerializer,
    MealReviewSerializer,
    OrderSerializer,
    OrderReviewSerializer,
    ReviewSerializer,
    SellerReviewSerializer,
)


class NoDeleteModelViewSet(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           viewsets.GenericViewSet):
    pass


class AddressViewSet(NoDeleteModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AllergenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer


class APIUserViewSet(NoDeleteModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer


class DietaryFilterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DietaryFilter.objects.all()
    serializer_class = DietaryFilterSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class ImageViewSet(NoDeleteModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class LocationViewSet(NoDeleteModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class MealViewSet(NoDeleteModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class MealReviewViewSet(NoDeleteModelViewSet):
    queryset = MealReview.objects.all()
    serializer_class = MealReviewSerializer


class OrderViewSet(NoDeleteModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderReviewViewSet(NoDeleteModelViewSet):
    queryset = OrderReview.objects.all()
    serializer_class = OrderReviewSerializer


class ReviewViewSet(NoDeleteModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SellerReviewViewSet(NoDeleteModelViewSet):
    queryset = SellerReview.objects.all()
    serializer_class = SellerReviewSerializer
