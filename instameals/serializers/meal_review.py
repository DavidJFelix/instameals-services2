from rest_framework import serializers

from ..models import MealReview


class MealReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MealReview
        fields = ('id',)
