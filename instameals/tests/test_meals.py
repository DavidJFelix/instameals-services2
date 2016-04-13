from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import APIUser, Image, Price, Address


class CreateMealTestCase(APITestCase):
    """"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        self.preview_image = Image.objects.create(url='http://example.com/test.jpg')
        self.pickup_address = Address.objects.create(
            line1='123 Test Ave',
            city='Testville',
            state='TX',
            postal_code='12345',
            country='USA',
            coordinates=Point(-123.0123, 45.6789)
        )
        self.price = Price.objects.create(currency='USD', value='39.99')
        self.new_meal = {
            'name': 'Test Meal',
            'description': 'A Meal to test meal creation',
            'allergens': [],
            'dietary_filters': [],
            'ingredients': [],
            'pickup_address': str(self.pickup_address.id),
            'portions': 0,
            'seller': str(self.user.id),
            'portions_available': 0,
            'price': str(self.price.id),
            'available_from': '2016-04-10T17:53:50.142558Z',
            'available_to': '2016-04-10T17:53:50.142558Z',
            'preview_image': str(self.preview_image.id),
            'images': []
        }

    def test_user_can_create_meal(self):
        url = reverse('meal-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.new_meal, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_can_create_meal_and_connected_objects_in_one_call(self):
        pass

    def test_non_user_cannot_create_meal(self):
        pass
