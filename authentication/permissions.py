from rest_framework.permissions import BasePermission


class CanAccessProfile(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        if request.user.is_superuser:
            return True
        
        if view.action in ['list', 'create']:
            return False
        
        return True
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        
        return obj.user == request.user