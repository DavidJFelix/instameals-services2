from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import APIUser
from ..serializers import APIUserSerializer


class APIUserViewSet(NoDeleteModelViewSet):
    # FIXME: filter out inactive users if that makes sense
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
    # FIXME: disallow writing to users that aren't you
    permission_classes = (AllowAny,)
