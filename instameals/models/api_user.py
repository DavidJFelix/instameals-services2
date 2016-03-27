from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel

from .address import Address
from .uuid import UUIDModelMixin


class APIUser(UUIDModelMixin, TimeStampedModel, AbstractUser):
    addresses = models.ManyToManyField(Address, related_name='users')

    class Meta:
        app_label = 'instameals'
        permissions = (
            ('APIUser', 'APIUser'),
        )
