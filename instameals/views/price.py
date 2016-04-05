from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import Price
from ..serializers import PriceSerializer


class PriceViewSet(NoDeleteModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    permission_classes = (AllowAny,)
