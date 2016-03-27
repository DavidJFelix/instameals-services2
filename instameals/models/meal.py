from django.db import models
from model_utils.models import TimeStampedModel

from .address import Address
from .allergen import Allergen
from .api_user import APIUser
from .dietary_filter import DietaryFilter
from .image import Image
from .ingredient import Ingredient
from .location import Location
from .uuid import UUIDModelMixin


class Meal(UUIDModelMixin, TimeStampedModel):
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=10000)
    allergens = models.ManyToManyField(Allergen, blank=True, related_name='meals')
    dietary_filters = models.ManyToManyField(DietaryFilter, blank=True, related_name='meals')
    ingredients = models.ManyToManyField(Ingredient, blank=True, related_name='meals')
    portions = models.PositiveSmallIntegerField()
    portions_available = models.PositiveSmallIntegerField()

    pickup_address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='meals')
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='meal')

    # FIXME: validate dates
    available_from = models.DateTimeField()
    available_to = models.DateTimeField()

    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey(APIUser, on_delete=models.CASCADE, related_name='meals')

    preview_image = models.ForeignKey(Image, related_name='preview_meals')
    images = models.ManyToManyField(Image, related_name='meals')

    class Meta:
        app_label = 'instameals'
        permissions = (
            ('view_meal', 'View Meal'),
        )

    def __str__(self):
        return "[{id}]: {seller}'s {name}".format(
                id=str(self.id),
                seller=str(self.seller),
                name=str(self.name),
        )
