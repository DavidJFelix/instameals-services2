from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Allergen
from ..serializers import AllergenSerializer


class AllergenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
    permission_classes = (AllowAny,)
