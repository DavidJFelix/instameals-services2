from django.contrib.gis.db import models
from model_utils.models import TimeStampedModel

from .uuid import UUIDModelMixin


class Address(UUIDModelMixin, TimeStampedModel):
    line1 = models.TextField()
    line2 = models.TextField(blank=True, default="")
    city = models.TextField()
    state = models.TextField()
    postal_code = models.TextField()
    country = models.TextField()
    coordinates = models.PointField()

    class Meta:
        app_label = 'instameals'
        permissions = (
            ('Address', 'Address'),
        )

    def __str__(self):
        return "[{id}]: {line1}, {line2}, {city}, {state}, {postal_code}, {country}".format(
                id=str(self.id),
                line1=str(self.line1),
                line2=str(self.line2),
                city=str(self.city),
                state=str(self.state),
                postal_code=str(self.postal_code),
                country=str(self.country),
        )
