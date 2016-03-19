import uuid

from django.db import models

from .api_user import APIUser
from .review import Review


class SellerReview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    review = models.OneToOneField(Review, on_delete=models.CASCADE)
    seller = models.ForeignKey(APIUser, on_delete=models.CASCADE, related_name='seller_reviews_of')
    reviewer = models.ForeignKey(APIUser, on_delete=models.CASCADE)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "{}: {}'s review of {}; {}".format(
                str(self.id),
                str(self.reviewer),
                str(self.seller),
                str(self.review),
        )
