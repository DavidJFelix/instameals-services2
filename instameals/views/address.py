from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.permissions import DjangoObjectPermissions

from .base import NoDeleteModelViewSet
from ..models import Address
from ..serializers import AddressSerializer


class AddressViewSet(NoDeleteModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (DjangoObjectPermissions,)
