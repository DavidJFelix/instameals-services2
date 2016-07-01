from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Order


class OrderSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Order
        fields = (
            'id',
            'buyer',
            'purchased_at',
            'meal',
            'billing_address',
            'pickup_time',
            'buyer_price',
            'pickup_address',
        )
        read_only_fields =(
            'seller_earnings',
            'is_paid',
        )
