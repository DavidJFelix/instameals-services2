from .base import NoDeleteModelViewSet
from ..models import FavoriteSeller
from ..serializers import FavoriteSellerSerializer


class FavoriteSellerViewSet(NoDeleteModelViewSet):
    queryset = FavoriteSeller.objects.all()
    serializer_class = FavoriteSellerSerializer
