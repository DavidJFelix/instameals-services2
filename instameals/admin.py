from django.contrib import admin

# Register your models here.
from instameals.models import (
    Address,
    Allergen,
    APIUser,
    DietaryFilter,
    FavoriteSeller,
    Image,
    Ingredient,
    Location,
    Meal,
    MealReview,
    Order,
    OrderReview,
    Review,
    SellerReview,
)

admin.site.register(Address)
admin.site.register(Allergen)
admin.site.register(APIUser)
admin.site.register(DietaryFilter)
admin.site.register(FavoriteSeller)
admin.site.register(Image)
admin.site.register(Ingredient)
admin.site.register(Location)
admin.site.register(Meal)
admin.site.register(MealReview)
admin.site.register(Order)
admin.site.register(OrderReview)
admin.site.register(Review)
admin.site.register(SellerReview)
