from .base import NoDeleteModelViewSet
from ..models import Price
from ..permissions import IsAuthenticatedCreateOnlyOrReadOnly
from ..serializers import PriceSerializer


# Move to immutable prices
class PriceViewSet(NoDeleteModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    permission_classes = (IsAuthenticatedCreateOnlyOrReadOnly,)
