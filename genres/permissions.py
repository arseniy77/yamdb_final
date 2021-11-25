from rest_framework import permissions

from users.models import User


class ModeratorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user:
            return False
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.role == User.ADMIN
        )
