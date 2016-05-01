from rest_framework import permissions
from rest_framework.permissions import BasePermission


class MealPermissions(BasePermission):
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


class OrderPermissions(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user and
                request.user.is_authenticated() and
                request.user.has_perm('view_order', obj)
            )
        elif request.method in ('PUT', 'PATCH'):
            return (
                request.user and
                request.user.is_authenticated() and
                request.user.has_perm('change_order', obj)
            )
        elif request.method == 'DELETE':
            return (
                request.user and
                request.user.is_authenticated() and
                request.user.has_perm('delete_order', obj)
            )
