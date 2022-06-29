import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsSellerAndOwnerOnlyOrReadOnly
from product.models import Product as ProductModel
from product.models import ProductImage as ProductImageModel
from product.serializers import ProductSerializer, ProductImageSerializer

""""""
# Create your views here.
class ProductApiView(APIView):
    permission_classes = [IsSellerAndOwnerOnlyOrReadOnly]

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
    permission_classes = [IsSellerAndOwnerOnlyOrReadOnly]

    def get_product_object_and_check_permission(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            product = ProductModel.objects.get(id=obj_id, is_delete=False)
        except ProductModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, product)
        return product

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


class ProductImageApiView(APIView):
    permission_classes = [IsSellerAndOwnerOnlyOrReadOnly]

    def get_product_object_and_check_permission(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            product = ProductModel.objects.get(id=obj_id, is_delete=False)
        except ProductModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, product)
        return product

    def get_product_image_object_and_check_permission(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            product_image = ProductImageModel.objects.get(id=obj_id)
        except ProductImageModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, product_image)
        return product_image

    def post(self, request, obj_id):
        product = self.get_product_object_and_check_permission(obj_id)
        if not product:
            return Response({"error": "존재하지 않는 상품입니다."}, status=status.HTTP_404_NOT_FOUND)

        product_image_serializer = ProductImageSerializer(data=request.data, context={"product": product})
        product_image_serializer.is_valid(raise_exception=True)
        product_image_serializer.save()
        return Response({"message": "이미지 등록 성공!!"}, status=status.HTTP_200_OK)

    def delete(self, request, obj_id):
        product_image = self.get_product_image_object_and_check_permission(obj_id)
        if not product_image:
            return Response({"error": "삭제할 이미지가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        product_image.delete()
        return Response({"message": "이미지 삭제 성공!!"}, status=status.HTTP_200_OK)

