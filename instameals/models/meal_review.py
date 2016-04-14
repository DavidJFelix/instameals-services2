from django.contrib.gis.db import models

from .api_user import APIUser
from .meal import Meal
from .review import Review
from .uuid import UUIDModelMixin


class MealReview(UUIDModelMixin, models.Model):
    # TODO: discuss adding images to meal reviews
    review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name='meal_review')
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='meal_review_of')
    reviewer = models.ForeignKey(APIUser, on_delete=models.CASCADE, related_name='meal_reviews')

    class Meta:
        app_label = 'instameals'
        permissions = (
            ('view_meal_review', 'Can view meal review'),
        )

    def __str__(self):
        return "[{id}]: {reviewer}'s review of {meal}; {review}".format(
                id=str(self.id),
                reviewer=str(self.reviewer),
                meal=str(self.meal),
                review=str(self.review),
        )
