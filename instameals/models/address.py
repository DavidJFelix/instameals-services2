import uuid

from django.db import models


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    line1 = models.TextField()
    line2 = models.TextField(blank=True, default="")
    city = models.TextField()
    state = models.TextField()
    postal_code = models.TextField()
    country = models.TextField()

    class Meta:
        app_label = 'instameals'

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