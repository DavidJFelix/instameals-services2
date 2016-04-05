from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import Order
from ..serializers import OrderSerializer


class OrderViewSet(NoDeleteModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # FIXME: only a buyer and seller should be able to see orders (also admins)
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    permission_classes = (AllowAny,)
