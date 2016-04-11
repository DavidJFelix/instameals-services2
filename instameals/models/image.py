from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class Image(UUIDModelMixin, TimeStampedModel):
    # FIXME: for some reason, admin console isn't honoring all of these options and only lists
    # other. I'm also not keen on classifying the image at this level
    IMAGE_TYPE = (
        ('meal_image', 'meal_image'),
        ('profile_image', 'profile_image'),
        ('review_meal_image', 'review_meal_image'),
        ('other', 'other'),
    )
    url = models.URLField()
    type = models.TextField(choices=IMAGE_TYPE, default='other')

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return str(self.id)
