from django.db import models

from .uuid import UUIDModelMixin


class DietaryFilter(UUIDModelMixin, models.Model):
    name = models.TextField(max_length=50, unique=True)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {name}".format(
                id=str(self.id),
                name=str(self.name),
        )
