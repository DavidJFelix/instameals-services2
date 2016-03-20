from rest_framework import serializers

from ..models import SellerReview


class SellerReviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SellerReview
        fields = ('id',)
