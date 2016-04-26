from django.contrib.gis.db import models

from .uuid import UUIDModelMixin


class Cuisine(UUIDModelMixin, models.Model):
    name = models.TextField(max_length=50, blank=False)
    description = models.TextField(max_length=250, blank=True)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {name}, {description}".format(
                id=str(self.id),
                name=str(self.name),
                description=str(self.description)
        )
