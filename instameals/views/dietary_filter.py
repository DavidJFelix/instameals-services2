from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import DietaryFilter
from ..serializers import DietaryFilterSerializer


class DietaryFilterViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DietaryFilter.objects.all()
    serializer_class = DietaryFilterSerializer
    permission_classes = (AllowAny,)
