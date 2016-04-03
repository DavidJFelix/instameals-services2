import math

from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .base import NoDeleteModelViewSet
from ..models import Meal
from ..serializers import MealSerializer


class MealViewSet(NoDeleteModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @staticmethod
    def get_coord_square(longitude, latitude, max_range=10000.0):
        # latitude varies about 0.7miles from north pole to equator -- ignore this
        #  and use equatorial longitude
        # 69.172 mi/deg-lat * 1609.34 m/mi = 111,321.266 m/deg-lat
        lat_offset = max_range / 111321.266
        lng_offset = max_range / (math.cos(math.radians(latitude)) * 111321.266)

        # Latitude has an upper limit of 90 at the north pole. Cap it at 90.
        max_lat = latitude + lat_offset
        max_lat = 90.0 if max_lat > 90.0 else max_lat

        # Latitude has a lower limit of -90 at the south pole. Cap it at -90.
        min_lat = latitude - lat_offset
        min_lat = -90.0 if min_lat < -90.0 else min_lat

        # Longitude has an upper limit of 180, wrap around to -180 if it overflows
        max_lng = longitude + lng_offset
        max_lng = max_lng - 360.0 if max_lng > 180.0 else max_lng

        # Longitude has a lower limit of -180, wrap around to 180 if it underflows
        min_lng = longitude - lng_offset
        min_lng = min_lng + 360 if min_lng < -180.0 else min_lng

        return min_lng, min_lat, max_lng, max_lat

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        longitude = self.request.query_params.get('lng', None)
        latitude = self.request.query_params.get('lat', None)
        # max_range = self.request.query_params.get('range', None)
        # units = self.request.query_params.get('units', 'mi')
        # limit = self.request.query_params.get('limit', None)
        # page = self.request.query_params.get('page', None)

        # FIXME: fail on bad input
        # Only obey latitude and longitude if we have both
        if all((latitude, longitude)):
            try:
                latitude = float(latitude)
                longitude = float(longitude)
            except ValueError:  # they weren't floats
                longitude, latitude = (-84.51, 39.10)
        else:
            longitude, latitude = (-84.51, 39.10)

        # FIXME: handle units and range
        # Convert max range to meters
        max_range = 15.0 * 1609.34

        (min_lng, min_lat, max_lng, max_lat) = MealViewSet.get_coord_square(
                longitude,
                latitude,
                max_range=max_range
        )

        # FIXME: handle 180, -180 filter edge case
        meals = queryset.filter(
                is_active=True,
                pickup_address__coordinates__distance_lte=(Point(longitude, latitude), Distance(m=max_range)),
        )
        serializer = MealSerializer(meals, many=True, context={'request': request})
        # TODO: sort items by distance and remove items outside of radius
        # FIXME: paginate here
        return Response(serializer.data)
