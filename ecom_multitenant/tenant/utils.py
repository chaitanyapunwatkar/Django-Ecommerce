from rest_framework import permissions

class IsSamtaUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['samta_admin']:
            return True
        return False