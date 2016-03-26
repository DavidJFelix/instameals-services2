from rest_framework import viewsets

from ..models import DietaryFilter
from ..serializers import DietaryFilterSerializer


class DietaryFilterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DietaryFilter.objects.all()
    serializer_class = DietaryFilterSerializer
