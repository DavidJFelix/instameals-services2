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

    def test_user_can_read_order_address(self):
        pass

    def test_user_cannot_read_non_owned_non_order_address(self):
        pass

    def test_user_can_read_filtered_list_of_addresses(self):
        pass

    def test_non_user_cannot_read_addresses(self):
        pass

    # Update REST/CRUD tests
    def test_user_can_update_owned_address(self):
        pass

    def test_user_can_partially_update_owned_address(self):
        pass

    def test_user_cannot_update_non_owned_address(self):
        pass

    def test_user_cannot_partially_update_non_owned_address(self):
        pass

    # Delete REST/CRUD tests
    def test_user_can_mark_owned_address_inactive(self):
        pass

    def test_user_cannot_delete_owned_address(self):
        pass

    def test_user_cannot_mark_non_owned_address_inactive(self):
        pass

    def test_user_cannot_delete_non_owned_address(self):
        pass
