from rest_framework import serializers

from ..models import OrderReview


class OrderReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderReview
        fields = ('id',)
