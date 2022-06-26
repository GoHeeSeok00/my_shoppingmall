from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import User as UserModel
from user.serializers import UserSerializer

""""""
# Create your views here.
class UserApiView(APIView):

    def get(self):
        user_serializer = UserSerializer(UserModel.objects.all(), many=True).data
        return Response(user_serializer, status=status.HTTP_200_OK)

    def post(self):
        return Response()