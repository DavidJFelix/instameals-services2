import uuid

from django.db import models


class Ingredient(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.TextField(max_length=50)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {name}".format(
                id=str(self.id),
                name=str(self.name),
        )
