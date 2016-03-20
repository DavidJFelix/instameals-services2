import uuid

from django.db import models

from .api_user import APIUser


class FavoriteSeller(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    seller = models.ForeignKey(APIUser, on_delete=models.CASCADE,
                               related_name="favorite_sellers_of")
    favoriter = models.ForeignKey(APIUser, on_delete=models.CASCADE,
                                  related_name="favorite_sellers")

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {favoriter}'s favorite of {seller}".format(
            id=str(self.id),
            seller=str(self.seller),
            favoriter=str(self.favoriter),
        )
