from django.db import models
from model_utils.models import TimeStampedModel

from .api_user import APIUser
from .meal import Meal
from .uuid import UUIDModelMixin


class Order(UUIDModelMixin, TimeStampedModel):
    buyer = models.ForeignKey(APIUser)
    purchased_at = models.DateTimeField(auto_now_add=True)
    meal = models.ForeignKey(Meal)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {buyer}'s purchase of {meal} at {purchased_at}".format(
                id=str(self.id),
                buyer=str(self.buyer),
                meal=str(self.meal),
                purchased_at=str(self.purchased_at),
        )
