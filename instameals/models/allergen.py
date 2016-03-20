import uuid

from django.db import models


class Allergen(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
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
