from rest_framework.serializers import ModelSerializer

from .address import AddressSerializer
from .api_user import APIUserSerializer
from .meal import RetrieveMealSerializer
from .price import PriceSerializer
from .uuid import UUIDModelSerializerMixin
from ..models import Order


class CreateUpdateOrderSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'buyer',
            'purchased_at',
            'meal',
            'billing_address',
            'pickup_time',
        )
