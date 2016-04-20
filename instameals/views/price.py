from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .base import NoDeleteModelViewSet
from ..models import Price
from ..serializers import PriceSerializer


# Move to immutable prices
class PriceViewSet(NoDeleteModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    # FIXME: this should not allow updates
    permission_classes = (IsAuthenticatedOrReadOnly,)
