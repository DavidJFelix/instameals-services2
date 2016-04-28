from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .base import CreateRetrieveModelViewSet
from ..models import Address
from ..serializers import AddressSerializer


class AddressViewSet(CreateRetrieveModelViewSet):
    """A REST view set for creating and retrieving addresses
    ---
    create:
        parameters:
            - name: coordinates
              description: GeoJSON object identifying lng/lat of an address
              required: true
              type: object

    """
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # FIXME: use this: filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class MyAddressViewSet(AddressViewSet):
    def get_queryset(self):
        return Address.objects.filter(users=self.request.user)
