from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .base import NoDeleteModelViewSet
from ..models import Review
from ..serializers import ReviewSerializer


# FIXME: make this deletable
class ReviewViewSet(NoDeleteModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # FIXME: restrict access to reviews. Write/read should be creator only
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
