from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.permissions import DjangoObjectPermissions

from .base import NoDeleteModelViewSet
from ..models import SellerReview
from ..serializers import SellerReviewSerializer


class SellerReviewViewSet(NoDeleteModelViewSet):
    queryset = SellerReview.objects.all()
    serializer_class = SellerReviewSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (DjangoObjectPermissions,)
