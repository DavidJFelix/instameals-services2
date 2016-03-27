from rest_framework import serializers

from ..models import UserAddressMapping


class UserAddressMappingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAddressMapping
        fields = ('id',)
