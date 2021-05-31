from rest_framework import permissions

from . import Roles


class BaseAccessPermission(permissions.BasePermission):
    role: str

    def has_permission(self, request, view=None):
        user_role = request.user.role

        if user_role:
            return user_role.name == role

        return False


class OnlyOwnerAccess(BaseAccessPermission):
    role = Roles.OWNER


class OnlyClientAccess(BaseAccessPermission):
    role = Roles.CLIENT
