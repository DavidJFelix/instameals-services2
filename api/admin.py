from django.contrib import admin

# Register your models here.
from .models import (
    Address,
    Allergen,
    APIUser,
    DietaryFilter,
    FavoriteSeller,
    Image,
    Ingredient,
    Meal,
    MealReview,
    Order,
    OrderReview,
    Price,
    Review,
    SellerReview,
)


class TimeStampedModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')


admin.site.register(Address)
admin.site.register(Allergen)
admin.site.register(APIUser, TimeStampedModelAdmin)
admin.site.register(DietaryFilter)
admin.site.register(FavoriteSeller, TimeStampedModelAdmin)
admin.site.register(Image, TimeStampedModelAdmin)
admin.site.register(Ingredient)
admin.site.register(Meal, TimeStampedModelAdmin)
admin.site.register(MealReview)
admin.site.register(Order, TimeStampedModelAdmin)
admin.site.register(OrderReview)
admin.site.register(Price)
admin.site.register(Review, TimeStampedModelAdmin)
admin.site.register(SellerReview)
