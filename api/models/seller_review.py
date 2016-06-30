from django.conf import settings
from django.contrib.gis.db import models

from .review import Review
from .uuid import UUIDModelMixin


class SellerReview(UUIDModelMixin, models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='seller_review')
    seller = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='seller_reviews_of',
    )
    reviewer = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='seller_reviews',
    )

    class Meta:
        app_label = 'api'
        permissions = (
            ('view_seller_review', 'Can view seller review'),
        )

    def __str__(self):
        return "[{id}]: {reviewer}'s review of {seller}; {review}".format(
                id=str(self.id),
                reviewer=str(self.reviewer),
                seller=str(self.seller),
                review=str(self.review),
        )
