import uuid

from django.db import models


class Location(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    # FIXME: validate lat, lng
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: lng: {lng}, lat: {lat}".format(
                id=str(self.id),
                lng=str(self.lng),
                lat=str(self.lat),
        )
