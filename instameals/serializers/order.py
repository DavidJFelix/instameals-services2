from rest_framework import serializers

from .address import AddressSerializer
from .api_user import APIUserSerializer
from .meal import MealSerializer
from .price import PriceSerializer
from .uuid import UUIDModelSerializerMixin
from ..models import Order


class OrderSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    buyer = APIUserSerializer()
    meal = MealSerializer()
    buyer_price = PriceSerializer()
    seller_earnings = PriceSerializer()
    billing_address = AddressSerializer()
    pickup_address = AddressSerializer()

    class Meta:
        model = Order
        fields = (
            'id',
            'buyer',
            'purchased_at',
            'meal',
            'buyer_price',
            'seller_earnings',
            'billing_address',
            'pickup_address',
        )
