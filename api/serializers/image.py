from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Image


class ImageSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'url',
            'type',
        )
