from datetime import timedelta

from PIL import Image as pImage
from django.contrib.gis.geos import Point
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.utils import timezone
from guardian.shortcuts import assign_perm  # Ignore pycharm warning
from io import BytesIO
from oauth2_provider.models import Application, AccessToken  # Ignore pycharm warning
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from ..models import APIUser, Meal, Address, Image, Price


class AuthTestCase(APITestCase):
    """A test case which tests the behavior of authorization headers and auth control endpoints
    which lie within the confines of this app's config. We will attempt to not test the framework
    but no promises."""

    def setUp(self):
        self.user = APIUser.objects.create(username='tester')
        # FIXME: reduce this user from superuser to explicitly defined role
        self.app_user = APIUser.objects.create(username='TestApp', is_superuser=True)
        self.app = Application.objects.create(
                name='Test App',
                user=self.app_user,
                client_type=Application.CLIENT_PUBLIC,
                authorization_grant_type=Application.GRANT_PASSWORD,
        )

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
        self.access_token = AccessToken.objects.create(
                user=self.user,
                token='Hl6yLPJBwhfS10vFexFjj8v0staIk9',  # Jibberish
                application=self.app,
                expires=timezone.now() + timedelta(hours=4),
                scope='write read',
        )

    def test_passing_auth_header_allows_restricted_endpoint(self):
        """Test that providing an authorization header allows a user perform an authenticated
        action"""

        # FIXME: This test relies on the negative test to ensure it is not a false pass
        # FIXME: This test is tightly coupled to meal view behavior
        url = reverse('v2:meal-detail', args=[self.meal.id])
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token.token)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Meal.objects.get(id=self.meal.id).is_active, False)

    def test_omitting_auth_header_does_not_allow_restricted_endpoint(self):
        """Test that not providing an authorization header does not allow you to perform a single
        auth only action."""

        # FIXME: This test relies on the postive test to ensure that it is not a false pass
        # FIXME: This test is tightly coupled to meal view behavior
        url = reverse('v2:meal-detail', args=[self.meal.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(Meal.objects.get(id=self.meal.id).is_active, True)
