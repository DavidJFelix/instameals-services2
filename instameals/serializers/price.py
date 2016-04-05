from rest_framework import serializers

from ..models import Price


class PriceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Price
        fields = ('id','currency', 'value')
