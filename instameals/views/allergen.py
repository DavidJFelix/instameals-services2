from rest_framework.viewsets import ModelViewSet

from ..models import Allergen
from ..permissions import IsAdminOrReadOnly
from ..serializers import AllergenSerializer


class AllergenViewSet(ModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
    permission_classes = (IsAdminOrReadOnly,)
