from oauth2_provider.models import Application  # Ignore pycharm warning
from rest_framework.test import APITestCase

from instameals.models import APIUser


class GoogleLoginTestCase(APITestCase):
    """Test that the OAuth2 login functionality works for google"""

    def setUp(self):
        # FIXME: reduce this user from superuser to explicitly defined role
        self.app_user = APIUser.objects.create(username='TestApp', is_superuser=True)
        self.app = Application.objects.create(
                name='Test App',
                user=self.app_user,
                client_type=Application.CLIENT_PUBLIC,
                authorization_grant_type=Application.GRANT_PASSWORD,
        )

    def test_first_login_creates_user(self):
        """Logging in with a google user for the first time should trigger a new user to be
         created"""
        # TODO
        pass

    def test_later_login_uses_same_user(self):
        """Logging in with a google user fot the second+ time should provide credentials for an
        existing user"""
        # TODO
        pass
