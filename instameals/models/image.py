from django.db import models

from .uuid import UUIDModelMixin


class Image(UUIDModelMixin, models.Model):
    url = models.URLField()

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return str(self.id)
