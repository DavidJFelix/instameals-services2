from .base import NoDeleteModelViewSet
from ..models import Review
from ..serializers import ReviewSerializer


class ReviewViewSet(NoDeleteModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
