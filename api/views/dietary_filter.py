from rest_framework.viewsets import ModelViewSet

from ..models import DietaryFilter
from ..permissions import IsAdminOrReadOnly
from ..serializers import DietaryFilterSerializer


class DietaryFilterViewSet(ModelViewSet):
    queryset = DietaryFilter.objects.all()
    serializer_class = DietaryFilterSerializer
    permission_classes = (IsAdminOrReadOnly,)
