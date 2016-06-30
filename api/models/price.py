from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class Price(UUIDModelMixin, TimeStampedModel):
    SUPPORTED_CURRENCIES = (
        ('USD', 'USD'),
    )
    currency = models.TextField(choices=SUPPORTED_CURRENCIES, default='USD')
    # max_digits is the number of total digits, including the 2 after the decimal.
    # We're going to allow an egregiously large 16 digits to account for low value currency
    value = models.DecimalField(decimal_places=2, max_digits=16)
