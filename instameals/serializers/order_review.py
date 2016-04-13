from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import OrderReview


class OrderReviewSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = OrderReview
        fields = ('id',)
