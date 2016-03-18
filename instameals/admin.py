from django.contrib import admin

# Register your models here.
from instameals.models import (
    Address,
    Allergen,
    APIUser,
    DietaryFilter,
    Image,
    Ingredient,
    Location,
    Meal,
    Order,
    Review,
)

admin.site.register(Address)
admin.site.register(Allergen)
admin.site.register(APIUser)
admin.site.register(DietaryFilter)
admin.site.register(Image)
admin.site.register(Ingredient)
admin.site.register(Location)
admin.site.register(Meal)
admin.site.register(Order)
admin.site.register(Review)
