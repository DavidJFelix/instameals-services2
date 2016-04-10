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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from dashing.utils import router as dashing_router
from .widgets import MealWidget
from django.views.generic.base import RedirectView


from instameals.views import (
    APIUserViewSet,
    AddressViewSet,
    AllergenViewSet,
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

router = DefaultRouter()
router.register(r'addresses', AddressViewSet)
router.register(r'allergens', AllergenViewSet)
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

#dashing widgets
dashing_router.register(MealWidget, 'meal_widget')
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^dashboard/', include(dashing_router.urls)),
    url(r'^$', RedirectView.as_view(url='dashboard/'), name='index'),
]

urlpatterns += router.urls
