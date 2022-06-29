import json

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from config.permissions import IsSellerAndOwnerOnlyOrReadOnly
from product.models import Product as ProductModel
from product.models import ProductImage as ProductImageModel
from product.models import ProductOption as ProductOptionModel
from product.serializers import ProductSerializer, ProductImageSerializer, ProductOptionSerializer

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
            object = ProductModel.objects.get(id=obj_id, is_delete=False)
        except ProductModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, object)
        return object

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
            object = ProductModel.objects.get(id=obj_id, is_delete=False)
        except ProductModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, object)
        return object

    def get_product_image_object_and_check_permission(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            object = ProductImageModel.objects.get(id=obj_id)
        except ProductImageModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, object)
        return object

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


class ProductOptionApiView(APIView):
    permission_classes = [IsSellerAndOwnerOnlyOrReadOnly]

    def get_product_object_and_check_permission(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            object = ProductModel.objects.get(id=obj_id, is_delete=False)
        except ProductModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, object)
        return object

    def post(self, request, obj_id):
        product = self.get_product_object_and_check_permission(obj_id)
        if not product:
            return Response({"error": "존재하지 않는 옵션입니다."}, status=status.HTTP_404_NOT_FOUND)

        product_option_serializer = (ProductOptionSerializer(data=request.data, context={"product": product}))
        product_option_serializer.is_valid(raise_exception=True)
        product_option_serializer.save()
        return Response({"message": "옵션 등록 성공!!"}, status=status.HTTP_200_OK)


class ProductOptionDetailApiView(APIView):
    permission_classes = [IsSellerAndOwnerOnlyOrReadOnly]

    def get_product_option_object_and_check_permission(self, obj_id):
        # objects.get에서 객체가 존재하지 않을 경우 DoesNotExist Exception 발생
        try:
            object = ProductOptionModel.objects.get(id=obj_id)
        except ProductOptionModel.DoesNotExist:
            # some event
            return
        self.check_object_permissions(self.request, object)
        return object

    def get(self, request, obj_id):
        product_option = self.get_product_option_object_and_check_permission(obj_id)
        if not product_option:
            return Response({"error": "삭제할 옵션이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response(ProductOptionSerializer(product_option).data, status=status.HTTP_200_OK)

    def put(self, request, obj_id):
        product_option = self.get_product_option_object_and_check_permission(obj_id)
        if not product_option:
            return Response({"error": "삭제할 옵션이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        
        product_option_serializer = ProductOptionSerializer(product_option, data=request.data, partial=True)
        product_option_serializer.is_valid(raise_exception=True)
        product_option_serializer.save()        
        return Response({"message": "상품 옵션 수정 성공!!"}, status=status.HTTP_200_OK)

    def delete(self, request, obj_id):
        product_option = self.get_product_option_object_and_check_permission(obj_id)
        if not product_option:
            return Response({"error": "삭제할 옵션이 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        product_option.delete()
        return Response({"message": "옵션 삭제 성공!!"}, status=status.HTTP_200_OK)