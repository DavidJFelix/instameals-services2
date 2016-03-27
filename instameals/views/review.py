from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.permissions import DjangoObjectPermissions

from .base import NoDeleteModelViewSet
from ..models import Review
from ..serializers import ReviewSerializer


class ReviewViewSet(NoDeleteModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = (DjangoObjectPermissionsFilter,)
    permission_classes = (DjangoObjectPermissions,)
