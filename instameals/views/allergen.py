from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Allergen
from ..serializers import AllergenSerializer


# FIXME: use a writable viewset when permission_classes restricts to admin writes only
class AllergenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Allergen.objects.all()
    serializer_class = AllergenSerializer
    # FIXME: turn off allowany. likely want to only permit admin, however, the viewset
    # should prevent it
    permission_classes = (AllowAny,)
