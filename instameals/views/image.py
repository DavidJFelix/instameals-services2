from guardian.shortcuts import assign_perm
from rest_framework import status
from rest_framework.response import Response

from .base import NoDeleteModelViewSet
from ..models import Image
from ..permissions import ImagePermissions
from ..serializers import ImageSerializer


class ImageViewSet(NoDeleteModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (ImagePermissions,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.initial_data['owner'] = request.user.id
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Set permissions on the new meal
        assign_perm('change_image', request.user, serializer.instance)

        # Respond with created data
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
