from .base import NoCreateModelViewSet
from ..models import APIUser
from ..permissions import APIUserPermissions
from ..serializers import APIUserSerializer


class APIUserViewSet(NoCreateModelViewSet):
    queryset = APIUser.objects.all()
    serializer_class = APIUserSerializer
    permission_classes = (APIUserPermissions,)


class MyAPIUserViewSet(APIUserViewSet):
    def get_queryset(self):
        return APIUser.objects.filter(id=self.request.user.id)
