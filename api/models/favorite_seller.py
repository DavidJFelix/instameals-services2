from django.conf import settings
from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class FavoriteSeller(UUIDModelMixin, TimeStampedModel):
    seller = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name="favorite_sellers_of",
    )
    favoriter = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name="favorite_sellers",
    )

    class Meta:
        app_label = 'api'
        permissions = (
            ('view_favorite_seller', 'Can view favorite seller'),
        )

    def __str__(self):
        return "[{id}]: {favoriter}'s favorite of {seller}".format(
                id=str(self.id),
                seller=str(self.seller),
                favoriter=str(self.favoriter),
        )
