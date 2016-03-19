import uuid

from django.db import models

from .api_user import APIUser
from .order import Order
from .review import Review


class OrderReview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='order_review')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_reviews_of')
    reviewer = models.ForeignKey(APIUser, on_delete=models.CASCADE, related_name='order_reviews')

    class Meta:
        app_label = 'instameals'
