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
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from api.views import (
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
    MyAddressViewSet,
    MyAPIUserViewSet,
    MyFavoriteSellerViewSet,
    MyFollowerViewSet,
    MyMealViewSet,
    MyMealReviewViewSet,
    MyOrderViewSet,
    MyOrderReviewViewSet,
    MySaleViewSet,
    MySaleReviewViewSet,
    MySellerReviewViewSet,
    MySoldMealReviewViewSet,
    OrderViewSet,
    OrderReviewViewSet,
    PriceViewSet,
    ReviewViewSet,
    SellerReviewViewSet,
)
from . import settings

v2_router = DefaultRouter()
v2_router.register(r'addresses', AddressViewSet)
v2_router.register(r'allergens', AllergenViewSet)
v2_router.register(r'cuisines', CuisineViewSet)
v2_router.register(r'dietary_filters', DietaryFilterViewSet)
v2_router.register(r'favorite_sellers', FavoriteSellerViewSet)
v2_router.register(r'images', ImageViewSet)
v2_router.register(r'ingredients', IngredientViewSet)
v2_router.register(r'meals', MealViewSet)
v2_router.register(r'meal_reviews', MealReviewViewSet)
v2_router.register(r'orders', OrderViewSet)
v2_router.register(r'order_reviews', OrderReviewViewSet)
v2_router.register(r'prices', PriceViewSet)
v2_router.register(r'reviews', ReviewViewSet)
v2_router.register(r'seller_reviews', SellerReviewViewSet)
v2_router.register(r'users', APIUserViewSet)

# TODO: make this router listed in the root router
# Router for /my namespace
my_router = DefaultRouter()
my_router.register(r'addresses', MyAddressViewSet)
my_router.register(r'favorite_sellers', MyFavoriteSellerViewSet)
my_router.register(r'followers', MyFollowerViewSet)
my_router.register(r'meals', MyMealViewSet)
my_router.register(r'meal_reviews', MyMealReviewViewSet)
my_router.register(r'profile', MyAPIUserViewSet)
my_router.register(r'orders', MyOrderViewSet)
my_router.register(r'order_reviews', MyOrderReviewViewSet)
my_router.register(r'sales', MySaleViewSet)
my_router.register(r'sale_reviews', MySaleReviewViewSet)
my_router.register(r'seller_reviews', MySellerReviewViewSet)
my_router.register(r'sold_meal_reviews', MySoldMealReviewViewSet)

# TODO: get some of these routes listed in the root router APIView
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^v2/my/', include(my_router.urls, namespace='my')),
    url(r'^v2/', include(v2_router.urls, namespace='v2')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
