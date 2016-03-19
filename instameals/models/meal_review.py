import uuid

from django.db import models

from .api_user import APIUser
from .meal import Meal
from .review import Review


class MealReview(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    review = models.OneToOneField(Review, on_delete=models.CASCADE)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(APIUser, on_delete=models.CASCADE)

    class Meta:
        app_label = 'instameals'
