from django.db import models

from .uuid import UUIDModelMixin


class Location(UUIDModelMixin, models.Model):
    # FIXME: validate lat, lng
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lng = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: lng: {lng}, lat: {lat}".format(
                id=str(self.id),
                lng=str(self.lng),
                lat=str(self.lat),
        )
