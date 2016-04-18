from rest_framework.permissions import AllowAny

from .base import NoDeleteModelViewSet
from ..models import OrderReview
from ..serializers import OrderReviewSerializer


# FIXME: change viewset to allow deletions
class OrderReviewViewSet(NoDeleteModelViewSet):
    queryset = OrderReview.objects.all()
    serializer_class = OrderReviewSerializer
    # filter_backends = (DjangoObjectPermissionsFilter,)
    # permission_classes = (DjangoObjectPermissions,)
    # FIXME: this permission class should only allow writing from the creator
    permission_classes = (AllowAny,)
