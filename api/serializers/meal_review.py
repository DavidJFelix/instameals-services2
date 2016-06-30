from rest_framework.serializers import ModelSerializer

from .uuid import UUIDModelSerializerMixin
from ..models import MealReview


class MealReviewSerializer(UUIDModelSerializerMixin, ModelSerializer):
    class Meta:
        model = MealReview
        fields = ('id',)
