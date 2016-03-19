import uuid

from django.db import models


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    class Meta:
        app_label = 'instameals'
