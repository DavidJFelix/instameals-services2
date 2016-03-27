from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.permissions import DjangoObjectPermissions

from .base import NoDeleteModelViewSet
from ..models import Order
from ..serializers import OrderSerializer


class OrderViewSet(NoDeleteModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (DjangoObjectPermissions,)
