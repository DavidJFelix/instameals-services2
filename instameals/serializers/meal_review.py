from rest_framework import serializers

from .uuid import UUIDModelSerializerMixin
from ..models import MealReview


class MealReviewSerializer(UUIDModelSerializerMixin, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MealReview
        fields = ('id',)
