from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import (
    Address,
    APIUser,
    Image,
    Meal,
    Order,
    Price,
)


class CreateOrderTestCase(APITestCase):
    def setUp(self):
        self.seller = APIUser.objects.create(username='seller')
        self.user = APIUser.objects.create(username='tester')
        self.meal = Meal.objects.create(
                name='Test Meal',
                description='A meal to test meal RUD',
                pickup_address=Address.objects.create(
                        line1='123 Test Ave',
                        city='Testville',
                        state='TX',
                        postal_code='12345',
                        country='USA',
                        coordinates=Point(-123.0123, 45.6789)
                ),
                portions=10,
                portions_available=10,
                price=Price.objects.create(
                        currency='USD',
                        value='39.99'
                ),
                seller=self.seller,
                available_from='2016-04-10T17:53:50.142558Z',
                available_to='2016-04-10T17:53:50.142558Z',
                preview_image=Image.objects.create(
                        type='other',
                        url='http://example.com/test.jpg'
                ),
        )
        self.billing_address = Address.objects.create(
                line1='456 Billing Rd',
                city='Testville',
                state='TX',
                postal_code='12345',
                country='USA',
                coordinates=Point(-123.1234, 45.6789)
        )
        self.new_order = {
            'meal': str(self.meal.id),
            'billing_address': str(self.billing_address.id),
            'pickup_time': '2016-04-10T17:53:51.142558Z',
        }

    def test_user_can_create_order_from_meal(self):
        """An authenticated user should be able to order a meal"""
        url = reverse('order-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.new_order)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)

    def test_create_order_response_structure(self):
        """Integration test to check the expected response structure of create order"""
        url = reverse('order-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.new_order)
        order = Order.objects.first()
        self.maxDiff = 4000
        self.assertEqual(
                response.json(),
                {
                    'id': str(order.id),
                    'buyer': {
                        'id': str(self.user.id),
                        'first_name': '',
                        'last_name': '',
                        'profile_image': None,
                        'username': 'tester',
                    },
                    'purchased_at': order.purchased_at.strftime('%Y-%m-%dT%T.%fZ'),
                    'meal': str(self.meal.id),
                    'buyer_price': {
                        'id': str(self.meal.price.id),
                        'currency': 'USD',
                        'value': '39.99',
                    },
                    'seller_earnings': {
                        'id': str(order.seller_earnings.id),
                        'currency': 'USD',
                        'value': '36.00'
                    },
                    'billing_address': {
                        'id': str(self.billing_address.id),
                        'city': 'Testville',
                        'coordinates': {
                            'coordinates': [-123.1234, 45.6789],
                            'type': 'Point'
                        },
                        'country': 'USA',
                        'line1': '456 Billing Rd',
                        'line2': '',
                        'postal_code': '12345',
                        'state': 'TX'
                    },
                    'pickup_address': {
                        'id': str(self.meal.pickup_address.id),
                        'city': 'Testville',
                        'coordinates': {
                            'coordinates': [-123.0123, 45.6789],
                            'type': 'Point',
                        },
                        'country': 'USA',
                        'line1': '123 Test Ave',
                        'line2': '',
                        'postal_code': '12345',
                        'state': 'TX'
                    },
                    'pickup_time': '2016-04-10T17:53:51.142558Z',
                    'is_paid': False,
                }
        )

    def test_non_user_cannot_create_order_from_meal(self):
        pass

    def test_user_cannot_create_order_from_non_meal(self):
        pass

    def test_order_response_structure(self):
        pass


class RetrieveUpdateDeleteOrderTestCase(APITestCase):
    def setUp(self):
        pass

    def test_user_can_view_purchased_order(self):
        pass

    def test_user_can_view_sold_order(self):
        pass

    def test_user_cannot_view_non_purchased_non_sold_order(self):
        pass

    def test_non_user_cannot_view_order(self):
        pass

    def test_user_can_list_purchased_and_sold_orders(self):
        pass

    def test_non_user_cannot_list_orders(self):
        pass
