from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .base import CreateRetrieveModelViewSet
from ..models import Address
from ..serializers import AddressSerializer


class AddressViewSet(CreateRetrieveModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    # FIXME: use this: filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
