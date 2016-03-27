from rest_framework.permissions import DjangoObjectPermissions, IsAuthenticatedOrReadOnly

from .base import NoDeleteModelViewSet
from ..models import Location
from ..serializers import LocationSerializer


class LocationViewSet(NoDeleteModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
