from .base import NoDeleteModelViewSet
from ..models import SellerReview
from ..serializers import SellerReviewSerializer


class SellerReviewViewSet(NoDeleteModelViewSet):
    queryset = SellerReview.objects.all()
    serializer_class = SellerReviewSerializer
