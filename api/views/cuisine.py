from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Cuisine
from ..serializers import CuisineSerializer


class CuisineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer
    permission_classes = (AllowAny,)
