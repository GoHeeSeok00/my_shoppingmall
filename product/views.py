import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsOwnerOrReadOnly
from product.models import Product as ProductModel
from product.serializers import ProductSerializer

""""""
# Create your views here.
class ProductApiView(APIView):
    # permission_classes = []

    def get(self, request):
        product_serializer = ProductSerializer(ProductModel.objects.filter(is_delete=False), many=True).data
        return Response(product_serializer, status=status.HTTP_200_OK)

    def post(self, request):
        context = {"request": request}
        product_serializer = ProductSerializer(data=request.data, context=context)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response({"message": "상품 등록 성공!!"}, status=status.HTTP_200_OK)


class ProductDetailApiView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def get_product_object_and_check_permission(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            user = ProductModel.objects.get(id=obj_id, is_delete=False)
        except ProductModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, user)
        return user

    def get(self, request, obj_id):
        product = self.get_product_object_and_check_permission(obj_id)
        if not product:
            return Response({"error": "존재하지 않는 상품입니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response(ProductSerializer(product).data, status=status.HTTP_200_OK)

    def put(self, request, obj_id):
        product = self.get_product_object_and_check_permission(obj_id)
        if not product:
            return Response({"error": "존재하지 않는 상품입니다."}, status=status.HTTP_404_NOT_FOUND)

        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response({"message": "상품 수정 성공!!"}, status=status.HTTP_200_OK)

    def delete(self, request, obj_id):
        product = self.get_product_object_and_check_permission(obj_id)
        if not product:
            return Response({"error": "존재하지 않는 상품입니다."}, status=status.HTTP_404_NOT_FOUND)

        product.is_delete = True
        product.save()
        return Response({"message": "상품 삭제 성공!!"}, status=status.HTTP_200_OK)