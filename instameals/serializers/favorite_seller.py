from rest_framework import serializers

from ..models import FavoriteSeller


class FavoriteSellerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavoriteSeller
        fields = (
            'id',
            'seller',
            'favoriter',
        )
