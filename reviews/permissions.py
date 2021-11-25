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


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class AuthorOrAdminOrModeratorOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated
                or request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        return (request.user.is_authenticated
                and (request.user.role == User.ADMIN
                     or request.user.role == User.MODERATOR
                     or obj.author == request.user))
