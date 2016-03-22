from django.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class Image(UUIDModelMixin, TimeStampedModel):
    url = models.URLField()

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return str(self.id)
