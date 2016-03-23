from django.contrib.auth.models import AbstractUser
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class APIUser(UUIDModelMixin, TimeStampedModel, AbstractUser):
    class Meta:
        app_label = 'instameals'
