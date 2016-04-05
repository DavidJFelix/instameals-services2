from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from .base import NoDeleteModelViewSet
from ..models import Image
from ..serializers import ImageSerializer


class ImageViewSet(NoDeleteModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    # FIXME: only allow users who own images to change them, but allow anyone to see them
    permission_classes = (AllowAny,)
