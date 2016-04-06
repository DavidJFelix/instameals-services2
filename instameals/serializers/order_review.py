from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import OrderReview


class OrderReviewSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderReview
        fields = ('id',)
