from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import Address
from ..serializers import AddressSerializer


class AddressViewSet(NoDeleteModelViewSet):
    # FIXME: filter out inactive address objects (if those exist)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # FIXME: perisions and filters should be based on user ownership
    # FIXME: use this: filter_backends = (DjangoObjectPermissionsFilter,)
    # FIXME: use this: permission_classes = (DjangoObjectPermissions,)
    permission_classes = (AllowAny,)
