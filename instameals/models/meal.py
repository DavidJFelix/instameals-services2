from datetime import datetime

from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

from .price import Price
from .address import Address
from .allergen import Allergen
from .api_user import APIUser
from .dietary_filter import DietaryFilter
from .image import Image
from .ingredient import Ingredient
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

    available_from = models.DateTimeField()
    available_to = models.DateTimeField()
    price = models.OneToOneField(Price)

    is_active = models.BooleanField(default=True)
    seller = models.ForeignKey(APIUser, on_delete=models.CASCADE, related_name='meals')

    preview_image = models.ForeignKey(Image, related_name='preview_meals')
    images = models.ManyToManyField(Image, related_name='meals', blank=True)

    class Meta:
        app_label = 'instameals'
        permissions = (
            ('view_meal', 'Can view meal'),
        )

    def clean(self):
        # Available from and available to must be chronological
        if self.available_from >= self.available_to:
            raise ValidationError(_("available_from must be older than available_to"))

        # Available to must be in the future
        if datetime.now() >= self.available_to:
            raise ValidationError(_("available_to must be in the future"))

    def __str__(self):
        return "[{id}]: {seller}'s {name}".format(
                id=str(self.id),
                seller=str(self.seller),
                name=str(self.name),
        )
