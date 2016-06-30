from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import SellerReview
from ..serializers import SellerReviewSerializer


# FIXME: use a deletable viewset
class SellerReviewViewSet(NoDeleteModelViewSet):
    queryset = SellerReview.objects.all()
    serializer_class = SellerReviewSerializer
    # FIXME: restrict write access to creator
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    permission_classes = (AllowAny,)


class MySellerReviewViewSet(SellerReviewViewSet):
    def get_queryset(self):
        return SellerReview.objects.filter(reviewer=self.request.user)


class MyIncomingSellerReviews(SellerReviewViewSet):
    def get_queryset(self):
        return SellerReview.objects.filter(seller=self.request.user)
