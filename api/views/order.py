from decimal import Decimal, ROUND_UP

from django.utils.timezone import now
from guardian.shortcuts import assign_perm
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .base import NoDeleteModelViewSet
from ..models import Order, Meal, Price
from ..permissions import OrderPermissions
from ..serializers import OrderSerializer


class OrderViewSet(NoDeleteModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (OrderPermissions,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.initial_data['buyer'] = request.user.id
        serializer.initial_data['purchased_at'] = now()
        serializer.is_valid(raise_exception=True)

        # Retrieve meal and compare to request items
        try:
            # FIXME: this is a quick solution, but has too many round trips to the db
            meal = Meal.objects.get(id=serializer.validated_data['meal'].id)
        except Meal.DoesNotExist:
            raise ValidationError('meal does not exist')

        if not meal.is_active:
            raise ValidationError('meal is inactive')

        # Compare the buyer reported price and reject non-matches
        if not meal.price.id == serializer.validated_data['buyer_price'].id:
            raise ValidationError('price did not match database')

        # Compare the buyer reported pickup address and reject non-matches
        if not meal.pickup_address.id == serializer.validated_data['pickup_address'].id:
            raise ValidationError('pickup address did not match database')

        # TODO: extract pricing
        # Calculate the seller earnings and make a new price object and add it
        instameals_cut = Decimal('0.1')
        two_places = Decimal('0.01')
        full_percentage = Decimal('1.00')
        seller_earnings_value = meal.price.value * (full_percentage - instameals_cut)
        seller_earnings = Price.objects.create(
                currency=meal.price.currency,
                value=seller_earnings_value.quantize(two_places, rounding=ROUND_UP),
        )
        serializer.validated_data['seller_earnings'] = seller_earnings

        self.perform_create(serializer)

        # Set buyer permissions on the new order
        assign_perm('view_order', request.user, serializer.instance)
        assign_perm('change_order', request.user, serializer.instance)
        assign_perm('delete_order', request.user, serializer.instance)

        # Set seller permissions on the new order
        assign_perm('view_order', meal.seller, serializer.instance)

        # Respond with created data
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MyOrderViewSet(OrderViewSet):
    def get_queryset(self):
        return Order.objects.filter(buyer=self.request.user)


class MySaleViewSet(OrderViewSet):
    def get_queryset(self):
        return Order.objects.filter(meal__seller=self.request.user)
