from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import SellerReview


class SellerReviewSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SellerReview
        fields = ('id',)
