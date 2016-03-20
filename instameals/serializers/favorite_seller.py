from rest_framework import serializers

from ..models import favorite_seller


class FavoriteSellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = favorite_seller
        fields = (
            'id',
            'seller',
            'favoriter',
        )
