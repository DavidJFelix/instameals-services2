from django.db import models

from .api_user import APIUser
from .review import Review
from .uuid import UUIDModelMixin


class SellerReview(UUIDModelMixin, models.Model):
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='seller_review')
    seller = models.ForeignKey(APIUser, on_delete=models.CASCADE, related_name='seller_reviews_of')
    reviewer = models.ForeignKey(APIUser, on_delete=models.CASCADE, related_name='seller_reviews')

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {reviewer}'s review of {seller}; {review}".format(
                id=str(self.id),
                reviewer=str(self.reviewer),
                seller=str(self.seller),
                review=str(self.review),
        )
