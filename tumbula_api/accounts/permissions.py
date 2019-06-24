from rest_framework.permissions import BasePermission
from .models import User

class AdministratorPermissions(BasePermission):
    
    def has_permission(self, request, view):
        return request.user.is_administrator and request.user.is_active

class StoreOwnerPermissions(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_store_owner and request.user.is_active