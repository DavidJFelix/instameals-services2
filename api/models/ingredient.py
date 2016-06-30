from django.contrib.gis.db import models

from .uuid import UUIDModelMixin


class Ingredient(UUIDModelMixin, models.Model):
    name = models.TextField(max_length=50, unique=True)

    class Meta:
        app_label = 'api'

    def __str__(self):
        return "[{id}]: {name}".format(
                id=str(self.id),
                name=str(self.name),
        )
