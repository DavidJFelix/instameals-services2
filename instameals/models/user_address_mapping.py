from django.db import models

from .api_user import APIUser
from .uuid import UUIDModelMixin
from .address import Address


class UserAddressMapping(UUIDModelMixin, models.Model):
    ADDRESS_TYPES = (
        ("billing", "billing"),
        ("home", "home"),
        ("pickup", "pickup"),
    )
    user = models.ForeignKey(APIUser)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    address_type = models.TextField(choices=ADDRESS_TYPES)

    class Meta:
        app_label = 'instameals'

    def __str__(self):
        return "[{id}]: {user}'s address {address}: Type {address_type}".format(
                id=str(self.id),
                user=str(self.user),
                address=str(self.address),
                address_type=str(self.address_type),
        )
