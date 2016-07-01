from io import BytesIO

from PIL import Image as pImage
from django.contrib.gis.geos import Point
from django.core.files.uploadedfile import InMemoryUploadedFile
from guardian.shortcuts import assign_perm  # Ignore Pycharm warning
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import APIUser, Image, Price, Address, Meal


class CreateMealTestCase(APITestCase):
    """Test the CREATE CRUD/REST endpoints for meal for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')

        image = pImage.new('RGBA', size=(50, 50), color=(256, 0, 0))
        image_file = BytesIO(image.tobytes())
        file = InMemoryUploadedFile(image_file, None, 'test.jpg', 'image/jpg', 1024, None)
        self.preview_image = Image.objects.create(
                owner=self.user,
                content=file
        )

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
        url = reverse('v2:meal-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.new_meal)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Meal.objects.count(), 1)

    def test_create_meal_response_structure(self):
        """Integration test to check the expected response structure of create meal"""
        url = reverse('v2:meal-list')
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
                    'pickup_address': str(meal.pickup_address.id),
                    'portions': 0,
                    'seller': str(meal.seller.id),
                    'portions_available': 0,
                    'price': str(meal.price.id),
                    'available_from': '2016-04-10T17:53:50.142558Z',
                    'available_to': '2016-04-10T17:53:50.142558Z',
                    'preview_image': str(meal.preview_image.id),
                    'images': []
                }
        )

    def test_create_meal_gives_user_permissions(self):
        """A user who creates a meal should be given appropriate permissions for the meal and
        attached objects"""
        url = reverse('v2:meal-list')
        self.client.force_authenticate(self.user)
        self.client.post(url, self.new_meal)
        new_meal = Meal.objects.first()
        self.assertTrue(self.user.has_perm('change_meal', new_meal))
        self.assertTrue(self.user.has_perm('delete_meal', new_meal))

    def test_non_user_cannot_create_meal(self):
        """An unauthenticated user should not be able to create a meal"""
        url = reverse('v2:meal-list')
        response = self.client.post(url, self.new_meal)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Meal.objects.count(), 0)

    def test_non_chronological_from_date_and_to_date_cannot_be_created(self):
        """A meal should not be able to be created if it has a available_from datetime that is
        chronologically after its available_to datetime"""
        # TODO
        pass

    def test_past_dated_available_to_meal_cannot_be_created(self):
        """A meal with a past available_to should not be able to be created"""
        # TODO
        pass


class RetrieveUpdateDeleteMealTestCase(APITestCase):
    """Test the RETRIEVE/UPDATE/DELETE CRUD/REST endpoints for meal for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        self.non_owner_user = APIUser.objects.create(username='tester2')

        image = pImage.new('RGBA', size=(50, 50), color=(256, 0, 0))
        image_file = BytesIO(image.tobytes())
        file = InMemoryUploadedFile(image_file, None, 'test.jpg', 'image/jpg', 1024, None)
        self.preview_image = Image.objects.create(
                owner=self.user,
                content=file
        )

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
                preview_image=self.preview_image,
        )
        assign_perm('change_meal', self.user, self.meal)
        assign_perm('delete_meal', self.user, self.meal)

    def test_can_retrieve_meal(self):
        """Any user should be able to retrieve a meal by id"""
        url = reverse('v2:meal-detail', args=[self.meal.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_meal_response_structure(self):
        """Integration test to check the expected response structure of retrieve address"""
        url = reverse('v2:meal-detail', args=[self.meal.id])
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
                    'pickup_address': str(self.meal.pickup_address.id),
                    'portions': 10,
                    'portions_available': 10,
                    'price': str(self.meal.price.id),
                    'seller': str(self.meal.seller.id),
                    'available_from': '2016-04-10T17:53:50.142558Z',
                    'available_to': '2016-04-10T17:53:50.142558Z',
                    'preview_image': str(self.meal.preview_image.id),
                    'images': [],
                }
        )

    def test_can_list_meals(self):
        """Any user should be able to list meals"""
        url = reverse('v2:meal-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_meals_response_structure(self):
        """Integration test to check the expected response structure of list meals"""
        # TODO: give this test 2 results
        # FIXME: handle the query params better
        url = reverse('v2:meal-list') + "?lng=-123.0123&lat=45.6789"
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
                        'pickup_address': str(self.meal.pickup_address.id),
                        'portions': 10,
                        'portions_available': 10,
                        'price': str(self.meal.price.id),
                        'seller': str(self.meal.seller.id),
                        'available_from': '2016-04-10T17:53:50.142558Z',
                        'available_to': '2016-04-10T17:53:50.142558Z',
                        'preview_image': str(self.meal.preview_image.id),
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
        url = reverse('v2:meal-detail', args=[self.meal.id])
        updated_meal = {
            'id': str(self.meal.id),
            'name': 'Test Meal',
            'description': 'A Meal to test meal creation',
            'allergens': [],
            'dietary_filters': [],
            'ingredients': [],
            'pickup_address': str(self.meal.pickup_address.id),
            'portions': 0,
            'seller': str(self.meal.seller.id),
            'portions_available': 0,
            'price': str(self.meal.price.id),
            'available_from': '2016-04-10T17:53:50.142558Z',
            'available_to': '2016-04-10T17:53:50.142558Z',
            'preview_image': str(self.meal.preview_image.id),
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
        url = reverse('v2:meal-detail', args=[self.meal.id])
        self.client.force_authenticate(self.user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Meal.objects.count(), 1)
        self.assertFalse(Meal.objects.get(id=self.meal.id).is_active)

    def test_user_cannot_delete_to_mark_non_owned_meal_inactive(self):
        """An authenticated user should not be able to DELETE a meal of which they are not the
        seller"""
        url = reverse('v2:meal-detail', args=[self.meal.id])
        self.client.force_authenticate(self.non_owner_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertTrue(Meal.objects.get(id=self.meal.id).is_active)

    def test_non_user_cannot_delete_to_mark_meal_inactive(self):
        """An unauthenticated user should not be able to DELETE a meal"""
        url = reverse('v2:meal-detail', args=[self.meal.id])
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
