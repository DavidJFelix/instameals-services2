from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from ..models import Cusine
from ..serializers import CusineSerializer


class CusineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cusine.objects.all()
    serializer_class = CusineSerializer
    permission_classes = (AllowAny,)
