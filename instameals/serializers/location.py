from rest_framework import serializers

from instameals.models import Location


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id',)
