"""instameals_services URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from dashing.utils import router as dashing_router
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from instameals.views import (
    APIUserViewSet,
    AddressViewSet,
    AllergenViewSet,
    CuisineViewSet,
    DietaryFilterViewSet,
    FavoriteSellerViewSet,
    ImageViewSet,
    IngredientViewSet,
    MealViewSet,
    MealReviewViewSet,
    OrderViewSet,
    OrderReviewViewSet,
    PriceViewSet,
    ReviewViewSet,
    SellerReviewViewSet,
)
from instameals.widgets import AvgPriceWidget
from instameals.widgets import MealWidget
from instameals.widgets import OrderWidget
from instameals.widgets import UserWidget

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'allergens', AllergenViewSet)
router.register(r'cuisines', CuisineViewSet)
router.register(r'dietary_filters', DietaryFilterViewSet)
router.register(r'favorite_sellers', FavoriteSellerViewSet)
router.register(r'images', ImageViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'meals', MealViewSet)
router.register(r'meal_reviews', MealReviewViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order_reviews', OrderReviewViewSet)
router.register(r'prices', PriceViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'seller_reviews', SellerReviewViewSet)
router.register(r'users', APIUserViewSet)

# TODO
# Router for /my namespace
my_router = DefaultRouter()
# addresses
# favorite_sellers
# meals
# meal_reviews
# profile (alias to user)
# orders
# order_reviews
# reviews
# seller_reviews

# dashing widgets
dashing_router.register(MealWidget, 'meal_widget')
dashing_router.register(UserWidget, 'user_widget')
dashing_router.register(OrderWidget, 'order_widget')
dashing_router.register(AvgPriceWidget, 'avg_meal_price_widget')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^dashboard/', include(dashing_router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^my/', include(my_router.urls, namespace='my'))
]

urlpatterns += router.urls
