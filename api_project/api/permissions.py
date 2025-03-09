from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Grant read-only access for safe methods
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Otherwise, restrict access to the object's owner
        return obj.owner == request.user
