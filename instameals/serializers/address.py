from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import Address


class AddressSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
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
