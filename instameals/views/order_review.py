from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.permissions import DjangoObjectPermissions

from .base import NoDeleteModelViewSet
from ..models import OrderReview
from ..serializers import OrderReviewSerializer


class OrderReviewViewSet(NoDeleteModelViewSet):
    queryset = OrderReview.objects.all()
    serializer_class = OrderReviewSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (DjangoObjectPermissions,)
