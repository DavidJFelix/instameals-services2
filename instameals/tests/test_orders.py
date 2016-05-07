from uuid import uuid4

from django.contrib.gis.geos import Point
from guardian.shortcuts import assign_perm  # Ignore PyCharm warning
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
    """Test the CRUD/REST endpoints for order business logic"""

    # FIXME: there's a race condition. If a seller updates a meal price after a buyer views the
    # meal, they will be given the new price when they attempt to buy the meal

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

    def test_create_order_gives_user_permissions(self):
        """A user who creates a meal should be given appropriate permissions for the meal as well
        as the seller"""
        url = reverse('order-list')
        self.client.force_authenticate(self.user)
        self.client.post(url, self.new_order)
        new_order = Order.objects.first()
        self.assertTrue(self.user.has_perm('change_order', new_order))
        self.assertTrue(self.user.has_perm('view_order', new_order))
        self.assertTrue(self.user.has_perm('delete_order', new_order))
        self.assertTrue(self.seller.has_perm('view_order', new_order))

    def test_non_user_cannot_create_order_from_meal(self):
        """An unauthenticated user should not be able to create an order from a meal"""
        url = reverse('order-list')
        response = self.client.post(url, self.new_order)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Order.objects.count(), 0)

    def test_user_cannot_create_order_from_non_meal(self):
        """A user should not be able to create an order from a meal which does not exist"""
        url = reverse('order-list')
        self.client.force_authenticate(self.user)
        bad_order = self.new_order
        # VERY rare chance of generating the same key
        bad_order['meal'] = str(uuid4())
        response = self.client.post(url, bad_order)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.count(), 0)

    def test_user_cannot_create_order_from_inactive_meal(self):
        """A user should not be able to create an order from a meal which is inactive"""
        url = reverse('order-list')
        self.client.force_authenticate(self.user)
        self.meal.is_active = False
        self.meal.save()
        response = self.client.post(url, self.new_order)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Order.objects.count(), 0)

    def test_create_order_creates_new_price_objects(self):
        """The creation of an order should freeze the price by copying it and making a new
        object"""
        # TODO
        pass


class RetrieveUpdateDeleteOrderTestCase(APITestCase):
    """Test the RETRIEVE/UPDATE/DELETE CRUD/REST endpoints for order for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        self.seller = APIUser.objects.create(username='seller')
        self.non_owner_user = APIUser.objects.create(username='tester2')
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
        self.order = Order.objects.create(
                meal=self.meal,
                pickup_time='2016-04-10T17:53:51.142558Z',
                billing_address=Address.objects.create(
                        line1='456 Billing Rd',
                        city='Testville',
                        state='TX',
                        postal_code='12345',
                        country='USA',
                        coordinates=Point(-123.1234, 45.6789)
                ),
                buyer=self.user,
                buyer_price=Price.objects.create(
                        currency='USD',
                        value='39.99'
                ),
                seller_earnings=Price.objects.create(
                        currency='USD',
                        value='36.00'
                ),
                pickup_address=self.meal.pickup_address,
        )

        self.other_order = Order.objects.create(
                meal=self.meal,
                pickup_time='2016-04-10T17:53:51.142558Z',
                billing_address=Address.objects.create(
                        line1='456 Billing Rd',
                        city='Testville',
                        state='TX',
                        postal_code='12345',
                        country='USA',
                        coordinates=Point(-123.1234, 45.6789)
                ),
                buyer=self.user,
                buyer_price=Price.objects.create(
                        currency='USD',
                        value='39.99'
                ),
                seller_earnings=Price.objects.create(
                        currency='USD',
                        value='36.00'
                ),
                pickup_address=self.meal.pickup_address,
        )

        assign_perm('view_order', self.user, self.order)
        assign_perm('change_order', self.user, self.order)
        assign_perm('delete_order', self.user, self.order)
        assign_perm('view_order', self.seller, self.order)

    def test_user_can_retrieve_purchased_order(self):
        """An authenticated user should be able to view an order they placed"""
        url = reverse('order-detail', args=[self.order.id])
        self.client.force_authenticate(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_retrieve_sold_order(self):
        """An authenticated user should be able to view an order they sold"""
        url = reverse('order-detail', args=[self.order.id])
        self.client.force_authenticate(self.seller)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_order_response_structure(self):
        """Integration test to check the expected response structure of retrieve order"""
        # TODO
        pass

    def test_user_cannot_retrieve_non_purchased_non_sold_order(self):
        """An authenticated user should be not be able to view an order they did not place or
        sell"""
        url = reverse('order-detail', args=[self.order.id])
        self.client.force_authenticate(self.non_owner_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_non_user_cannot_retrieve_order(self):
        """An unauthenticated user should not be able to view an order"""
        url = reverse('order-detail', args=[self.order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_list_purchased_and_sold_orders_only(self):
        """An authenticated user should be able to view their orders and not other orders"""
        # TODO
        pass

    def test_non_user_cannot_list_orders(self):
        """An unauthenticated user should not be able to list any orders"""
        url = reverse('order-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
