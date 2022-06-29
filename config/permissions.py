from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission

""""""
# create custom permission
class IsAdminOrNotAuthenticatedCreateOnly(BasePermission):
    """
    로그인 하지 않은 사용자만 post 가능
    관리자는 모두 가능
    """
    SAFE_METHODS = ('POST', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if request.method in self.SAFE_METHODS and not user.is_authenticated:
            return True
        elif user.is_admin:
            return True

        return False


class IsOwnerOrReadOnly(BasePermission):
    """
    GET method이면 Read만 가능
    관리자는 모든 접근 가능
    작성자는 모든 접근 가능
    """
    SAFE_METHODS = ("GET",)
    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method in self.SAFE_METHODS:
            return True
        elif user.is_authenticated:
            if user.is_admin:
                return True
            elif obj.__class__ == get_user_model():
                return obj.id == user.id
            elif hasattr(obj, "user"):
                return obj.user.id == user.id
            return False
        return False


class IsOwner(BasePermission):
    """
    관리자는 모든 접근 가능
    작성자는 모든 접근 가능
    오브젝트 체크를 하지 않을경우 로그인 사용자만 가능
    """
    def has_object_permission(self, request, view, obj):
        user = request.user

        if user.is_authenticated:
            if user.is_admin:
                return True
            elif obj.__class__ == get_user_model():
                return obj.id == user.id
            elif hasattr(obj, "user"):
                return obj.user.id == user.id
            return False
        return False

    def has_permission(self, request, view):
        user = request.user

        if user.is_authenticated:
            return True
        return False


class IsSellerAndOwnerOnlyOrReadOnly(BasePermission):
    """
    GET method이면 Read만 가능(모든 사용자)
    관리자는 모든 접근 가능
    판매자이면서 작성자는 모든 접근 가능
    """
    SAFE_METHODS = ("GET",)

    def has_object_permission(self, request, view, obj):
        user = request.user

        if request.method in self.SAFE_METHODS:
            return True
        elif user.is_authenticated:
            if user.is_admin:
                return True
            elif obj.__class__ == get_user_model():
                return obj.id == user.id and user.is_seller == True
            elif hasattr(obj, "user"):
                return obj.user.id == user.id and user.is_seller == True
            elif hasattr(obj, "product"):
                return obj.product.user.id == user.id and user.is_seller == True
            return False
        return False

    def has_permission(self, request, view):
        user = request.user

        if request.method in self.SAFE_METHODS:
            return True
        elif user.is_authenticated:
            if user.is_admin:
                return True
            elif user.is_seller:
                return True
            return False
        return False