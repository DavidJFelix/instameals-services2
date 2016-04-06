from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import Review


class ReviewSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'rating')
