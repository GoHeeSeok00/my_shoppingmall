from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product as ProductModel
from product.serializers import ProductSerializer

""""""
# Create your views here.
class ProductApiView(APIView):
    # permission_classes = []

    def get(self, request):
        product_serializer = ProductSerializer(ProductModel.objects.all(), many=True).data
        return Response(product_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        return  Response()