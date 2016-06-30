from django.conf import settings
from django.contrib.gis.db import models

from .order import Order
from .review import Review
from .uuid import UUIDModelMixin


class OrderReview(UUIDModelMixin, models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='order_review')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_reviews_of')
    reviewer = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='order_reviews',
    )

    class Meta:
        app_label = 'api'
        permissions = (
            ('view_order_review', 'Can view order review'),
        )

    def __str__(self):
        return "[{id}]: {reviewer}'s review of {order}; {review}".format(
                id=str(self.id),
                reviewer=str(self.reviewer),
                order=str(self.order),
                review=str(self.review),
        )
