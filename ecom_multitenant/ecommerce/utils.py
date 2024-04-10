from rest_framework import permissions

class IsSupervisor(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['supervisor','administrator']:
            return True
        return False

class IsSalesPerson(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['sales_person','supervisor','admin']:
            return True
        return False