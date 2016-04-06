from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import FavoriteSeller


class FavoriteSellerSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavoriteSeller
        fields = (
            'id',
            'seller',
            'favoriter',
        )
