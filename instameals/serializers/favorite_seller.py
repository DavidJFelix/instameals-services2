from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import FavoriteSeller


class FavoriteSellerSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = FavoriteSeller
        fields = (
            'id',
            'seller',
            'favoriter',
        )
