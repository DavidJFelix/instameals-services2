from rest_framework.viewsets import ModelViewSet

from ..models import Ingredient
from ..permissions import IsAdminOrReadOnly
from ..serializers import IngredientSerializer


class IngredientViewSet(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
