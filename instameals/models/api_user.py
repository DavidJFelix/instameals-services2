from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .address import Address
from .image import Image
from .uuid import UUIDModelMixin


class APIUser(UUIDModelMixin, TimeStampedModel, AbstractUser):
    addresses = models.ManyToManyField(Address, related_name='users')
    profile_image = models.OneToOneField(Image, related_name='users', blank='', null=True)

    class Meta:
        app_label = 'instameals'
        permissions = (
            ('view_api_user', 'View APIUser'),
        )
