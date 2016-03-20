from rest_framework import serializers

from ..models import DietaryFilter


class DietaryFilterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DietaryFilter
        fields = ('id', 'name')
