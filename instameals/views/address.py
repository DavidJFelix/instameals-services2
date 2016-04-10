from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .base import CreateRetrieveModelViewSet
from ..models import Address
from ..serializers import AddressSerializer


class AddressViewSet(CreateRetrieveModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # FIXME: permissions and filters should be based on user ownership
    # FIXME: use this: filter_backends = (DjangoObjectPermissionsFilter,)
    # FIXME: use this: permission_classes = (DjangoObjectPermissions,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
