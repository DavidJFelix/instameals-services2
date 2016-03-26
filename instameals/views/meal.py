from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from .base import NoDeleteModelViewSet
from ..models import Meal
from ..serializers import MealSerializer


class MealViewSet(NoDeleteModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        longitude = self.request.query_params.get('lng', None)
        latitude = self.request.query_params.get('lat', None)
        max_range = self.request.query_params.get('range', None)
        units = self.request.query_params.get('units', 'mi')
        limit = self.request.query_params.get('limit', None)
        page = self.request.query_params.get('page', None)

        # FIXME: perform haversine here

        meals = queryset.filter(
                is_active=True,
        )
        serializer = MealSerializer(meals, many=True, context={'request': request})
        return Response(serializer.data)
