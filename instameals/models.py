import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)


class Allergen(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.TextField(max_length=50)

    def __str__(self):
        return str(self.name)


class APIUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)


class DietaryFilter(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.TextField(max_length=50)

    def __str__(self):
        return str(self.name)


class Ingredient(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.TextField(max_length=50)

    def __str__(self):
        return str(self.name)


class Image(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    url = models.URLField()

    def __str__(self):
        return str(self.id)


class Location(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)


class Meal(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=1000)
    allergens = models.ManyToManyField(Allergen, blank=True)
    dietary_filters = models.ManyToManyField(DietaryFilter, blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)


class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)


class Review(models.Model):
    RATING_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    text = models.TextField(max_length=10000)
    rating = models.IntegerField(choices=RATING_CHOICES)
