from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import SellerReview
from ..serializers import SellerReviewSerializer


class SellerReviewViewSet(NoDeleteModelViewSet):
    queryset = SellerReview.objects.all()
    serializer_class = SellerReviewSerializer
    # FIXME: restrict this
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    permission_classes = (AllowAny,)
