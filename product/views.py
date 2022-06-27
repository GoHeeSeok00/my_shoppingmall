from rest_framework.response import Response
from rest_framework.views import APIView

""""""
# Create your views here.
class ProductApiView(APIView):
    # permission_classes = []

    def get(self, request):
        return Response()

    def post(self, request):
        return  Response()