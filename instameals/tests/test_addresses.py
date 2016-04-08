from rest_framework.test import APITestCase


class AddressTests(APITestCase):
    # Create REST/CRUD tests
    def test_user_can_create_address(self):
        self.assertEqual(True, True)

    def test_non_user_cannot_create_address(self):
        pass

    # Read REST/CRUD tests
    def test_user_can_read_owned_address(self):
        pass

    def test_user_can_read_order_addresses(self):
        pass

    def test_user_cannot_read_non_owned_non_order_addresses(self):
        pass

    def test_user_can_update_owned_addresses(self):
        pass

    def test_non_user_cannot_read_addresses(self):
        pass

    # Update REST/CRUD tests
    def test_user_cannot_update_non_owned_address(self):
        pass
