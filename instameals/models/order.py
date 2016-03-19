import uuid

from django.db import models

from .api_user import APIUser
from .meal import Meal


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    buyer = models.ForeignKey(APIUser)
    purchased_at = models.DateTimeField(auto_now_add=True)
    meal = models.ForeignKey(Meal)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {buyer}'s purchase of {meal} at {purchased_at}".format(

        )
