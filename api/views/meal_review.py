from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import MealReview
from ..serializers import MealReviewSerializer


# FIXME: allow delete
class MealReviewViewSet(NoDeleteModelViewSet):
    queryset = MealReview.objects.all()
    serializer_class = MealReviewSerializer
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    # FIXME: only allow writes from creator
    permission_classes = (AllowAny,)


class MyMealReviewViewSet(MealReviewViewSet):
    def get_queryset(self):
        return MealReview.objects.filter(reviewer=self.request.user)


class MySoldMealReviewViewSet(MealReviewViewSet):
    def get_queryset(self):
        return MealReview.objects.filter(meal__seller=self.request.user)
