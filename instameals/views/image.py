from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .base import NoDeleteModelViewSet
from ..models import Image
from ..serializers import ImageSerializer


class ImageViewSet(NoDeleteModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
