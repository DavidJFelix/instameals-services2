from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .base import NoDeleteModelViewSet
from ..models import Meal
from ..serializers import MealSerializer


class MealViewSet(NoDeleteModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
