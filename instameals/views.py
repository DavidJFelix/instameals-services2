# Create your views here.
from rest_framework import mixins, viewsets

from .models import (
    Address,
    Allergen,
    APIUser,
    DietaryFilter,
    Image,
    Ingredient,
    Meal,
    Order,
    Review,
)
from .serializers import (
    AddressSerializer,
    AllergenSerializer,
    APIUserSerializer,
    DietaryFilterSerializer,
    ImageSerializer,
    IngredientSerializer,
    MealSerializer,
    OrderSerializer,
    ReviewSerializer,
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


class AllergenViewSet(NoDeleteModelViewSet):
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


class MealViewSet(NoDeleteModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class OrderViewSet(NoDeleteModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(NoDeleteModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer