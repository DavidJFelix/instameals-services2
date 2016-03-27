from .base import NoDeleteModelViewSet
from ..models import UserAddressMapping
from ..serializers import UserAddressMappingSerializer


class UserAddressMappingViewSet(NoDeleteModelViewSet):
    queryset = UserAddressMapping.objects.all()
    serializer_class = UserAddressMappingSerializer
