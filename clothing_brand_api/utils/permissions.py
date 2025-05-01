from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    """
    Allows access only to the owner of the object.
    """
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsProductOwner(permissions.BasePermission):
    """
    Allows access only to the owner of the product's brand.
    """
    def has_object_permission(self, request, view, obj):
        return obj.brand.owner == request.user

class IsCustomer(permissions.BasePermission):
    """
    Allows access only to customer users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'

class IsBrandOwner(permissions.BasePermission):
    """
    Allows access only to brand owner users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'brand_owner'

