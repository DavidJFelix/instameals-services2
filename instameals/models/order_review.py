import uuid

from django.db import models

from .api_user import APIUser
from .order import Order
from .review import Review


class OrderReview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    review = models.OneToOneField(Review, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(APIUser, on_delete=models.CASCADE)

    class Meta:
        app_label = 'instameals'
