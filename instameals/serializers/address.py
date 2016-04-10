from rest_framework.serializers import HyperlinkedModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Address


class AddressSerializer(UUIDModelSerializerMixin, HyperlinkedModelSerializer):
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
