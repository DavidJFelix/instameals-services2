from decimal import Decimal, ROUND_UP
from django.utils.timezone import now
from guardian.shortcuts import assign_perm
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import DjangoObjectPermissionsFilter
from rest_framework.response import Response

from instameals.permissions import OrderPermissions
from .base import NoDeleteModelViewSet
from ..models import Order, Meal, Price
from ..serializers import CreateUpdateOrderSerializer, RetrieveOrderSerializer


class OrderViewSet(NoDeleteModelViewSet):
    queryset = Order.objects.all()
    serializer_class = RetrieveOrderSerializer
    permission_classes = (OrderPermissions,)

    def create(self, reqest, *args, **kwargs):
        serializer = CreateUpdateOrderSerializer(data=reqest.data)
        serializer.initial_data['buyer'] = reqest.user.id
        serializer.initial_data['purchased_at'] = now()
        serializer.is_valid(raise_exception=True)

        # FIXME: this is a quick solution, but has too many round trips to the db
        # TODO: investigate if recovery is needed if meal doesn't exist
        meal = Meal.objects.get(id=serializer.validated_data['meal'].id)
        if not meal.is_active:
            raise ValidationError('meal is inactive')

        # Freeze the price and pickup address for an order so sellers can't bait and switch
        price = meal.price
        pickup_address = meal.pickup_address
        serializer.validated_data['buyer_price'] = price
        serializer.validated_data['pickup_address'] = pickup_address

        # TODO: extract pricing
        # Calculate the seller earnings and make a new price object and add it
        instameals_cut = Decimal('0.1')
        two_places = Decimal('0.01')
        full_percentage = Decimal('1.00')
        seller_earnings_value = price.value * (full_percentage - instameals_cut)
        seller_earnings = Price.objects.create(
            currency=price.currency,
            value=seller_earnings_value.quantize(two_places, rounding=ROUND_UP),
        )
        serializer.validated_data['seller_earnings'] = seller_earnings

        self.perform_create(serializer)

        # Set buyer permissions on the new order
        assign_perm('view_order', reqest.user, serializer.instance)
        assign_perm('change_order', reqest.user, serializer.instance)
        assign_perm('delete_order', reqest.user, serializer.instance)

        # Set seller permissions on the new order
        assign_perm('view_order', meal.seller, serializer.instance)

        # Respond with created data
        headers = self.get_success_headers(serializer.data)
        response_serializer = self.serializer_class(serializer.instance,
                                                    context={'request': reqest})
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MyOrderViewSet(OrderViewSet):
    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class MySaleViewSet(OrderViewSet):
    def get_queryset(self):
        return Order.objects.filter(meal__seller=self.request.user)
