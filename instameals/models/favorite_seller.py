from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .api_user import APIUser
from .uuid import UUIDModelMixin


class FavoriteSeller(UUIDModelMixin, TimeStampedModel):
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
