from rest_framework.permissions import BasePermission
from .models import CustomUser

class CanAccessAds(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        
        if view.action in ['create', 'list']:
            if isinstance(request.user, CustomUser):
                return request.user.user_role == 'admin'

        if view.action in ['update', 'partial_update', 'destroy']:
            if isinstance(request.user, CustomUser):
                return request.user.user_role == 'admin'
            
        if view.action in ['retrieve']:
            return True
        
        return False
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if view.action in ['retrieve']:
            return True

        if view.action in ['update', 'partial_update', 'destroy']:
            if isinstance(request.user, CustomUser):
                return request.user.user_role == 'admin'
        
        return False