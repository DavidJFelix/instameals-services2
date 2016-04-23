from rest_framework import permissions
from rest_framework.permissions import DjangoObjectPermissions


class MealPermissions(DjangoObjectPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method in ('PUT', 'PATCH'):
            return (
                request.user and
                request.user.is_authenticated() and
                request.user.has_perm('change_meal', obj)
            )
        elif request.method == 'DELETE':
            return (
                request.user and
                request.user.is_authenticated() and
                request.user.has_perm('delete_meal', obj)
            )
