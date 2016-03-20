from rest_framework import serializers

from ..models import APIUser


class APIUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = APIUser
        fields = ('id', 'username',)
