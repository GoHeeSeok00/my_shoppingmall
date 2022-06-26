from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User as UserModel
from user.serializers import UserSerializer

""""""
# create custom permission
class IsAdminOrCreateOnly(permissions.BasePermission):
    """
    모든 사용자는 쓰기만 가능
    관리자는 모두 가능
    """
    SAFE_METHODS = ('POST', )
    message = '접근 권한이 없습니다.'

    def has_permission(self, request, view):
        user = request.user

        if request.method in self.SAFE_METHODS or user.is_admin:
            return True

        return False


# Create your views here.
class UserApiView(APIView):
    permission_classes = [IsAdminOrCreateOnly]
    def get(self, request):
        user_serializer = UserSerializer(UserModel.objects.all(), many=True).data
        return Response(user_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response({"message": "회원가입 성공!!"}, status=status.HTTP_200_OK)