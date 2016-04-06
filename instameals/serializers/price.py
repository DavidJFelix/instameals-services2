from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import Price


class PriceSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ('id','currency', 'value')
