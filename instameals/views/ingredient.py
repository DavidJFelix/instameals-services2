from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Ingredient
from ..serializers import IngredientSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    # FIXME: make this admin only writable
    permission_classes = (AllowAny,)
