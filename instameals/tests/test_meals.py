from django.contrib.gis.geos import Point
from guardian.shortcuts import assign_perm
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import APIUser, Image, Price, Address, Meal


class CreateMealTestCase(APITestCase):
    """Test the CREATE CRUD/REST endpoints for meal for business logic"""

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
        """An authenticated user should be able to create a meal where they are the seller"""
        url = reverse('meal-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.new_meal)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meal.objects.count(), 1)

    def test_create_meal_response_structure(self):
        """Integration test to check the expected response structure of create meal"""
        url = reverse('meal-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.new_meal)
        meal = Meal.objects.first()
        self.maxDiff = 2000
        self.assertEqual(
                response.json(),
                {
                    'id': str(meal.id),
                    'name': 'Test Meal',
                    'description': 'A Meal to test meal creation',
                    'allergens': [],
                    'dietary_filters': [],
                    'ingredients': [],
                    'pickup_address': {
                        'id': str(meal.pickup_address.id),
                        'line1': '123 Test Ave',
                        'line2': '',
                        'city': 'Testville',
                        'state': 'TX',
                        'postal_code': '12345',
                        'country': 'USA',
                        'coordinates': {
                            'type': 'Point',
                            'coordinates': [-123.0123, 45.6789],
                        },
                    },
                    'portions': 0,
                    'seller': {
                        'id': str(meal.seller.id),
                        'username': 'tester',
                        'first_name': '',
                        'last_name': '',
                        'profile_image': None,
                    },
                    'portions_available': 0,
                    'price': {
                        'id': str(meal.price.id),
                        'currency': 'USD',
                        'value': '39.99',
                    },
                    'available_from': '2016-04-10T17:53:50.142558Z',
                    'available_to': '2016-04-10T17:53:50.142558Z',
                    'preview_image': {
                        'id': str(meal.preview_image.id),
                        'type': 'other',
                        'url': 'http://example.com/test.jpg'
                    },
                    'images': []
                }
        )

    def test_create_meal_gives_user_permissions(self):
        """A user who creates a meal should be given appropriate permissions for the meal and
        attached objects"""
        # TODO
        url = reverse('meal-list')
        self.client.force_authenticate(self.user)
        self.client.post(url, self.new_meal)
        new_meal = Meal.objects.first()
        self.assertTrue(self.user.has_perm('change_meal', new_meal))
        self.assertTrue(self.user.has_perm('delete_meal', new_meal))

    def test_user_can_create_meal_and_connected_objects_in_one_call(self):
        """An authenticated user should be able to create a meal with all attached objects"""
        # FIXME: need to have an upsert type
        pass

    def test_non_user_cannot_create_meal(self):
        """An unauthenticated user should not be able to create a meal"""
        url = reverse('meal-list')
        response = self.client.post(url, self.new_meal)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RetrieveUpdateDeleteMealTestCase(APITestCase):
    """Test the RETRIEVE/UPDATE/DELETE CRUD/REST endpoints for address for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
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
                seller=self.user,
                available_from='2016-04-10T17:53:50.142558Z',
                available_to='2016-04-10T17:53:50.142558Z',
                preview_image=Image.objects.create(
                        type='other',
                        url='http://example.com/test.jpg'
                ),
        )
        assign_perm('change_meal', self.user, self.meal)
        assign_perm('delete_meal', self.user, self.meal)

    def test_can_retrieve_meal(self):
        """Any user should be able to retrieve a meal by id"""
        url = reverse('meal-detail', args=[self.meal.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_meal_response_structure(self):
        """Integration test to check the expected response structure of retrieve address"""
        url = reverse('meal-detail', args=[self.meal.id])
        response = self.client.get(url)
        self.maxDiff = 2000
        self.assertEqual(
                response.json(),
                {
                    'id': str(self.meal.id),
                    'name': 'Test Meal',
                    'description': 'A meal to test meal RUD',
                    'allergens': [],
                    'dietary_filters': [],
                    'ingredients': [],
                    'pickup_address': {
                        'id': str(self.meal.pickup_address.id),
                        'line1': '123 Test Ave',
                        'line2': '',
                        'city': 'Testville',
                        'state': 'TX',
                        'postal_code': '12345',
                        'country': 'USA',
                        'coordinates': {
                            'type': 'Point',
                            'coordinates': [-123.0123, 45.6789],
                        },
                    },
                    'portions': 10,
                    'portions_available': 10,
                    'price': {
                        'id': str(self.meal.price.id),
                        'currency': 'USD',
                        'value': '39.99',
                    },
                    'seller': {
                        'id': str(self.meal.seller.id),
                        'username': 'tester',
                        'first_name': '',
                        'last_name': '',
                        'profile_image': None,
                    },
                    'available_from': '2016-04-10T17:53:50.142558Z',
                    'available_to': '2016-04-10T17:53:50.142558Z',
                    'preview_image': {
                        'id': str(self.meal.preview_image.id),
                        'type': 'other',
                        'url': 'http://example.com/test.jpg'
                    },
                    'images': [],
                }
        )

    def test_can_list_meals(self):
        """Any user should be able to list meals"""
        url = reverse('meal-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_meals_response_structure(self):
        """Integration test to check the expected response structure of list meals"""
        # TODO: give this test 2 results
        # FIXME: handle the query params better
        url = reverse('meal-list') + "?lng=-123.0123&lat=45.6789"
        response = self.client.get(url)
        self.maxDiff = 2000
        self.assertEqual(
                response.json(),
                [
                    {
                        'id': str(self.meal.id),
                        'name': 'Test Meal',
                        'description': 'A meal to test meal RUD',
                        'allergens': [],
                        'dietary_filters': [],
                        'ingredients': [],
                        'pickup_address': {
                            'id': str(self.meal.pickup_address.id),
                            'line1': '123 Test Ave',
                            'line2': '',
                            'city': 'Testville',
                            'state': 'TX',
                            'postal_code': '12345',
                            'country': 'USA',
                            'coordinates': {
                                'type': 'Point',
                                'coordinates': [-123.0123, 45.6789],
                            },
                        },
                        'portions': 10,
                        'portions_available': 10,
                        'price': {
                            'id': str(self.meal.price.id),
                            'currency': 'USD',
                            'value': '39.99',
                        },
                        'seller': {
                            'id': str(self.meal.seller.id),
                            'username': 'tester',
                            'first_name': '',
                            'last_name': '',
                            'profile_image': None,
                        },
                        'available_from': '2016-04-10T17:53:50.142558Z',
                        'available_to': '2016-04-10T17:53:50.142558Z',
                        'preview_image': {
                            'id': str(self.meal.preview_image.id),
                            'type': 'other',
                            'url': 'http://example.com/test.jpg'
                        },
                        'images': [],
                    }
                ]
        )

    def test_user_can_update_owned_meal(self):
        """An authenticated user should be able to update a meal of which they are the seller"""
        # TODO
        pass

    def test_user_cannot_update_non_owned_meal(self):
        """An authenticated user should not be able to update a meal of which they are not the
         seller"""
        # TODO
        pass

    def test_non_user_cannot_update_meal(self):
        """An unauthenticated user should not be able to update a meal"""
        url = reverse('meal-detail', args=[self.meal.id])
        updated_meal = {
            'id': str(self.meal.id),
            'name': 'Test Meal',
            'description': 'A Meal to test meal creation',
            'allergens': [],
            'dietary_filters': [],
            'ingredients': [],
            'pickup_address': {
                'id': str(self.meal.pickup_address.id),
                'line1': '123 Test Ave',
                'line2': '',
                'city': 'Testville',
                'state': 'TX',
                'postal_code': '12345',
                'country': 'USA',
                'coordinates': {
                    'type': 'Point',
                    'coordinates': [-123.0123, 45.6789],
                },
            },
            'portions': 0,
            'seller': {
                'id': str(self.meal.seller.id),
                'username': 'tester',
                'first_name': '',
                'last_name': '',
                'profile_image': None,
            },
            'portions_available': 0,
            'price': {
                'id': str(self.meal.price.id),
                'currency': 'USD',
                'value': '39.99',
            },
            'available_from': '2016-04-10T17:53:50.142558Z',
            'available_to': '2016-04-10T17:53:50.142558Z',
            'preview_image': {
                'id': str(self.meal.preview_image.id),
                'type': 'other',
                'url': 'http://example.com/test.jpg'
            },
            'images': []
        }
        response = self.client.put(url, updated_meal)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_partially_update_owned_meal(self):
        """An authenticated user should be able to partially update a meal of which they are the
        seller"""
        # TODO
        pass

    def test_user_cannot_partially_update_non_owned_meal(self):
        """An authenticated user should not be able to update a meal of which they are not the
        seller"""
        # TODO
        pass

    def test_non_user_cannot_partially_update_meal(self):
        """An unauthenticated user should not be able to partially update a meal"""
        # TODO
        pass

    def test_user_can_delete_to_mark_owned_meal_inactive(self):
        """An authenticated user should be able to DELETE a meal of which they are the seller to
        mark the meal as is_active=False"""
        url = reverse('meal-detail', args=[self.meal.id])
        self.client.force_authenticate(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Meal.objects.count(), 1)
        self.assertFalse(Meal.objects.get(id=self.meal.id).is_active)

    def test_user_cannot_delete_to_mark_non_owned_meal_inactive(self):
        """An authenticated user should not be able to DELETE a meal of which they are not the
        seller"""
        url = reverse('meal-detail', args=[self.meal.id])
        self.client.force_authenticate(self.non_owner_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Meal.objects.get(id=self.meal.id).is_active)

    def test_non_user_cannot_delete_to_mark_meal_inactive(self):
        """An unauthenticated user should not be able to DELETE a meal"""
        url = reverse('meal-detail', args=[self.meal.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertTrue(Meal.objects.get(id=self.meal.id).is_active)

    def test_update_meal_notifies_buyers(self):
        # TODO: we don't currently have notifications
        pass

    def test_partial_update_meal_notifies_buyers(self):
        # TODO: we don't currently have notifications
        pass

    def test_delete_to_mark_meal_inactive_notifies_buyers(self):
        # TODO: we don't currently have notifications
        pass
