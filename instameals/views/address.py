from .base import NoDeleteModelViewSet
from ..models import Address
from ..serializers import AddressSerializer


class AddressViewSet(NoDeleteModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
