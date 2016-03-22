from django.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class Review(UUIDModelMixin, TimeStampedModel):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    text = models.TextField(max_length=10000)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {rating}".format(
                id=str(self.id),
                rating=str(self.rating),
        )
