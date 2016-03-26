from .base import NoDeleteModelViewSet
from ..models import OrderReview
from ..serializers import OrderReviewSerializer


class OrderReviewViewSet(NoDeleteModelViewSet):
    queryset = OrderReview.objects.all()
    serializer_class = OrderReviewSerializer
