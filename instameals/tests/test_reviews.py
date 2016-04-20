from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import APIUser, Review

class CreatePriceTestCase(APITestCase):
    """Test the CREATE CRUD/REST endpoints for address for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        self.price = {
                        "id": "981ae4f2-35d3-4752-a06a-626b8008f08e",
                        "text": "itz so tasty",
                        "rating": 5
                    }

    def test_user_can_create_price(self):
        url = reverse('review-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.price, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Review.objects.count(), 1)

    def test_non_user_cannot_create_price(self):
        url = reverse('review-list')
        response = self.client.post(url, self.price, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Review.objects.count(), 0)

