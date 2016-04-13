from django.contrib.gis.geos import Point
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import Address, APIUser


class CreateAddressTestCase(APITestCase):
    """Test the CREATE CRUD/REST endpoints for address for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        self.new_address = {
            'line1': '123 Test Ave',
            'city': 'Testville',
            'state': 'TX',
            'postal_code': '12345',
            'country': 'USA',
            'coordinates': {
                'type': 'Point',
                'coordinates': [
                    -123.0123, 45.6789
                ],
            },
        }

    def test_user_can_create_address(self):
        """An authenticated user should be allowed to create an address"""
        url = reverse('address-list')
        self.client.force_authenticate(self.user)
        response = self.client.post(url, self.new_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 1)

    def test_user_created_address_is_listed_in_api_user_addresses(self):
        """When A user creates an address, it should be added to APIUser.addresses"""
        pass

    def test_non_user_cannot_create_address(self):
        """An unauthenticated user should not be allowed to create an address"""
        url = reverse('address-list')
        response = self.client.post(url, self.new_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Address.objects.count(), 0)


class RetrieveUpdateDeleteAddressTestCase(APITestCase):
    """Test the RETRIEVE/UPDATE/DELETE CRUD/REST endpoints for address for business logic"""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        self.address = Address.objects.create(
                line1='123 Test Ave',
                city='Testville',
                state='TX',
                postal_code='12345',
                country='USA',
                coordinates=Point(-123.0123, 45.6789)
        )
        self.updated_address = {
            'line1': '321 Test Ave',
            'city': 'Testville',
            'state': 'TX',
            'postal_code': '12345',
            'country': 'USA',
            'coordinates': {
                'type': 'Point',
                'coordinates': [
                    -123.0123, 45.6789
                ],
            },
        }

    # Retrieve REST/CRUD tests
    def test_can_retrieve_address(self):
        """Any user should be able to retrieve an address by its id"""
        url = reverse('address-detail', args=[self.address.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_list_address(self):
        """Nobody should be allowed to get a list addresses (405)"""
        url = reverse('address-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # Update REST/CRUD tests
    def test_user_cannot_update_address(self):
        """An authenticated user should be rejected from updating an address with a 405"""
        url = reverse('address-detail', args=[self.address.id])
        self.client.force_authenticate(self.user)
        response = self.client.put(url, self.updated_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # Get actual data and ensure it hasn't changed
        address_prime = Address.objects.get(id=self.address.id)
        self.assertEqual(self.address, address_prime)

    def test_non_user_cannot_update_address(self):
        """An unauthenticated user should be rejected from updating an address with a 401"""
        url = reverse('address-detail', args=[self.address.id])
        response = self.client.put(url, self.updated_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Get actual data and ensure it hasn't changed
        address_prime = Address.objects.get(id=self.address.id)
        self.assertEqual(self.address, address_prime)

    def test_user_cannot_partially_update_address(self):
        """An authenticated user should be rejected from partially updating
            an address with a 405
        """
        url = reverse('address-detail', args=[self.address.id])
        self.client.force_authenticate(self.user)
        response = self.client.patch(url, self.updated_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # Get actual data and ensure it hasn't changed
        address_prime = Address.objects.get(id=self.address.id)
        self.assertEqual(self.address, address_prime)

    def test_non_user_cannot_partially_update_address(self):
        """An unauthenticated user should be rejected from partially updating
            an address with a 401
        """
        url = reverse('address-detail', args=[self.address.id])
        response = self.client.patch(url, self.updated_address, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Get actual data and ensure it hasn't changed
        address_prime = Address.objects.get(id=self.address.id)
        self.assertEqual(self.address, address_prime)

    # Delete REST/CRUD tests
    def test_user_cannot_delete_address(self):
        """An authenticated user should not be able to delete an immutable address"""
        url = reverse('address-detail', args=[self.address.id])
        self.client.force_authenticate(self.user)
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        # Get actual data and ensure it hasn't changed
        address_prime = Address.objects.get(id=self.address.id)
        self.assertEqual(self.address, address_prime)

    def test_non_user_cannot_delete_address(self):
        """An unauthenticated user should not be able to delete an immutable address"""
        url = reverse('address-detail', args=[self.address.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Get actual data and ensure it hasn't changed
        address_prime = Address.objects.get(id=self.address.id)
        self.assertEqual(self.address, address_prime)
