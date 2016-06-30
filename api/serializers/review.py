from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import Review


class ReviewSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'rating')
