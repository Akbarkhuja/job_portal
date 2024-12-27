from rest_framework import permissions


class IsAdminOrRecruiter(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'applicant-detail' and request.method in permissions.SAFE_METHODS :
            return True
        
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_admin)


class IsApplicant(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_applicant)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user