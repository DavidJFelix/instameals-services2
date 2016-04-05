from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class Price(UUIDModelMixin, TimeStampedModel):
    SUPPORTED_CURRENCIES = (
        ('USD', 'USD'),
    )
    currency = models.TextField(choices=SUPPORTED_CURRENCIES, default='USD')
    value = models.DecimalField(decimal_places=2, max_digits=2)
