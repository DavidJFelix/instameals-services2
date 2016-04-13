from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Address


class AddressSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'line1',
            'line2',
            'city',
            'state',
            'postal_code',
            'country',
            'coordinates',
        )
