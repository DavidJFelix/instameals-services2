from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import SellerReview


class SellerReviewSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = SellerReview
        fields = ('id',)
