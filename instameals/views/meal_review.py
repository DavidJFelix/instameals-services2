from rest_framework.permissions import DjangoObjectPermissions

from .base import NoDeleteModelViewSet
from ..models import MealReview
from ..serializers import MealReviewSerializer


class MealReviewViewSet(NoDeleteModelViewSet):
    queryset = MealReview.objects.all()
    serializer_class = MealReviewSerializer
    permission_classes = (DjangoObjectPermissions,)
