from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User as UserModel
from user.serializers import UserSerializer, UserDetailSerializer

""""""
# create custom permission
class IsAdminOrNotAuthenticatedCreateOnly(permissions.BasePermission):
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


# Create your views here.
class UserApiView(APIView):
    permission_classes = [IsAdminOrNotAuthenticatedCreateOnly]
    def get(self, request):
        user_serializer = UserSerializer(UserModel.objects.all(), many=True).data
        return Response(user_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        password1 = request.data["password"]
        password2 = request.data["password2"]
        # 비밀번호 일치 여부 확인
        if password1 != password2:
            return Response({"error": "비밀번호가 일치하지 않습니다."}, status=status.HTTP_400_BAD_REQUEST)
        # print(request.data)
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response({"message": "회원가입 성공!!"}, status=status.HTTP_200_OK)


class UserDetailApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            user = UserModel.objects.get(id=obj_id)
        except UserModel.DoesNotExist:
            # some event
            return Response({"error": "존재하지 않는 사용자 입니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response(UserDetailSerializer(user).data, status=status.HTTP_200_OK)
    def put(self, request, obj_id):
        return Response()
    def delete(self, request, obj_id):
        return Response()

# 로그인 view
class LoginApiView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        username = request.data.get('username', '')
        password = request.data.get('password', '')
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response(
                {"error": "존재하지 않는 계정이거나 패스워드가 일치하지 않습니다."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        login(request, user)
        return Response({"message": "로그인 성공!!"}, status=status.HTTP_200_OK)


# 로그아웃 view
class LogoutApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공!!"}, status=status.HTTP_200_OK)