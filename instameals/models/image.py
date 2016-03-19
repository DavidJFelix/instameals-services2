import uuid

from django.db import models


class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    url = models.URLField()

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return str(self.id)
