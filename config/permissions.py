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