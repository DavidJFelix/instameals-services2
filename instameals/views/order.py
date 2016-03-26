from .base import NoDeleteModelViewSet
from ..models import Order
from ..serializers import OrderSerializer


class OrderViewSet(NoDeleteModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer