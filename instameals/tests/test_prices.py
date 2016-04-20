from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import APIUser, Price

class CreatePriceTestCase(APITestCase):
    """Test the CREATE CRUD/REST endpoints for address for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        self.price = {
                "id": "87c527a1-b9ed-469c-80f4-649227a83835",
                "currency": "USD",
                "value": "5.00"
            }
        self.invalid_price_currency = {
                "id": "87c527a1-b9ed-469c-80f4-649227a83835",
                "currency": "RPS",
                "value": "5.00"
            }

    def test_user_can_create_price(self):
        url = reverse('price-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.price, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Price.objects.count(), 1)

    def test_non_user_cannot_create_price(self):
        url = reverse('price-list')
        response = self.client.post(url, self.price, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Price.objects.count(), 0)

    def test_user_cannot_create_price_in_non_supported_currency_formats(self):
        url = reverse('price-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.invalid_price_currency, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Price.objects.count(), 0)
