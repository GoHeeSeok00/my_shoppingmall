from collections import OrderedDict

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsAdminOrNotAuthenticatedCreateOnly, IsOwnerOrReadOnly
from user.models import User as UserModel
from user.serializers import UserSerializer, UserDetailSerializer


""""""
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
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            user = UserModel.objects.get(id=obj_id)
        except UserModel.DoesNotExist:
            # some event
            return Response({"error": "존재하지 않는 사용자 입니다."}, status=status.HTTP_404_NOT_FOUND)
        self.check_object_permissions(self.request, user)
        return user

    def str_to_boolean_of_data_value(self, data, key, true_word, false_word):
        try:
            if data[key] == true_word:
                data[key] = True
            elif data[key] == false_word:
                data[key] = False
        except KeyError:
            pass
        return data


    def get(self, request, obj_id):
        user = self.get_object(obj_id)
        return Response(UserDetailSerializer(user).data, status=status.HTTP_200_OK)

    def put(self, request, obj_id):
        user = self.get_object(obj_id)

        data = OrderedDict()
        data.update(request.data)

        ###########################################################################
        """
        클라이언트에서 boolean 값을 전달 할 수 있으면 불필요한 과정
        postman으로 테스트 시 file 데이터 때문에 form-data를 이용하지만 
        boolean 값이 없어서 str을 boolean으로 바꿔주는 과정
        """
        # str to boolean // data type 변경
        # data = self.str_to_boolean_of_data_value(data, "gender", "남자", "여자")
        # data = self.str_to_boolean_of_data_value(data, "is_receive_marketing_info", "ture", "false")
        ###########################################################################
        print(data)
        user_serializer = UserDetailSerializer(user, data=data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response({"message": "프로필 수정 성공!!"}, status=status.HTTP_200_OK)

    def delete(self, request, obj_id):
        user = self.get_object(obj_id)
        user.is_active = True
        user.save()
        # is_active 필드 변경 후 로그아웃 // 이후부터 로그인 못함
        logout(request)
        return Response({"message": "탈퇴 완료"})

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