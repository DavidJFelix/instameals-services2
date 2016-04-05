from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import Review
from ..serializers import ReviewSerializer


class ReviewViewSet(NoDeleteModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # FIXME: restrict access to reviews
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    permission_classes = (AllowAny,)
