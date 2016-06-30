from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Price


class PriceSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Price
        fields = ('id', 'currency', 'value')
