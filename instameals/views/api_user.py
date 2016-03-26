from .base import NoDeleteModelViewSet
from ..models import APIUser
from ..serializers import APIUserSerializer


class APIUserViewSet(NoDeleteModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
