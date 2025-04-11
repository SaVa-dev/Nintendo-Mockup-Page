from rest_framework import permissions

class IsOwnerOrStaffOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow owners of an object or staff to edit it,
    but allow anyone to read it.
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
            
        # Write permissions are only allowed to the owner or staff
        return obj.usuario == request.user or request.user.is_staff