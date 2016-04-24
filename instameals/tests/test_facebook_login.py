from rest_framework.test import APITestCase


class FacebookLoginTestCase(APITestCase):
    """Test that the OAuth2 login functionality works for facebook"""
    def setUp(self):
        pass

    def test_first_login_creates_user(self):
        """Logging in with a facebook user for the first time should trigger a new user to be
         created"""
        # TODO
        pass

    def test_later_login_uses_same_user(self):
        """Logging in with a facebook user fot the second+ time should provide credentials for an
        existing user"""
        # TODO
        pass
