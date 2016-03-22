from django.contrib.auth.models import AbstractUser

from .uuid import UUIDModelMixin


class APIUser(UUIDModelMixin, AbstractUser):
    class Meta:
        app_label = 'instameals'
