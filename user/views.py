from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

""""""
# Create your views here.
class UserApiView(APIView):

    def get(self):
        return Response()

    def post(self):
        return Response()