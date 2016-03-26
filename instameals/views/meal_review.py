from .base import NoDeleteModelViewSet
from ..models import MealReview
from ..serializers import MealReviewSerializer


class MealReviewViewSet(NoDeleteModelViewSet):
    queryset = MealReview.objects.all()
    serializer_class = MealReviewSerializer
    filter_backends = ()
