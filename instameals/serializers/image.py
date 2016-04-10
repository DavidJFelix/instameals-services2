from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import Image


class ImageSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'url',
            'type',
        )
