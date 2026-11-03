from rest_framework.permissions import BasePermission

supposed_groups = ['Administrator', 'Engineer', 'Supervisor']

class IsSupervisorUser(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Supervisor').exists()