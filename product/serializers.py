import json

from rest_framework import serializers

from product.models import Product as ProductModel
from product.models import Category as CategoryModel
from product.models import ProductImage as ProductImageModel
from product.models import ProductOption as ProductOptionModel

""""""
class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionModel
        fields = ["product", "name", "price", "quantity", "is_discount", "discount_price", "discount_start_date",
                  "discount_end_date"]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = ["product", "image"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, required=False, read_only=True)
    productimage_set = ProductImageSerializer(many=True, required=False, read_only=True)
    productoption_set = ProductOptionSerializer(many=True, required=False, read_only=True)
    get_categorys = serializers.ListField(required=False)
    get_images = serializers.ListField(required=False)
    get_options = serializers.ListField(required=False)

    class Meta:
        model = ProductModel
        fields = ["user", "title", "category", "thumbnail", "description", "view_count", "is_active", "is_delete",
                  "created_at", "updated_at", "productimage_set", "productoption_set", "get_categorys", "get_images",
                  "get_options"]
        extra_kwargs = {
            "is_delete": {"write_only": True},
            "get_categorys": {"write_only": True},
            "get_images": {"write_only": True},
            "get_options": {"write_only": True},
        }
        read_only_fields = ["user", "view_count"]

    def create(self, validated_data):
        # 관계형성이 되어있는 정보(카테고리, 이미지, 옵션 정보)는 따로 빼서 저장
        get_categorys = validated_data.pop("get_categorys", [])
        images = validated_data.pop("get_images", [])
        options = validated_data.pop("get_options", [])

        # Product 인스턴스 생성
        user = self.context["request"].user
        product = ProductModel(user=user, **validated_data)
        product.save()

        # ProductImage create
        for image in images:
            ProductImageModel.objects.create(product=product, image=image)

        # ProductOption create
        for option in options:
            ProductOptionModel.objects.create(product=product, **json.loads(option))

        # category 등록
        product.category.add(*get_categorys)
        return product