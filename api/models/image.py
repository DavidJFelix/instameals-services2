from django.conf import settings
from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class Image(UUIDModelMixin, TimeStampedModel):
    content = models.ImageField()
    owner = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE,
            related_name='images',
    )

    class Meta:
        app_label = 'api'

    def __str__(self):
        return str(self.id)
