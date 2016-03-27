from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.permissions import DjangoObjectPermissions

from .base import NoDeleteModelViewSet
from ..models import FavoriteSeller
from ..serializers import FavoriteSellerSerializer


class FavoriteSellerViewSet(NoDeleteModelViewSet):
    queryset = FavoriteSeller.objects.all()
    serializer_class = FavoriteSellerSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (DjangoObjectPermissions,)
