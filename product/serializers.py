from rest_framework import serializers

from product.models import Product as ProductModel
from product.models import Category as CategoryModel
from product.models import ProductImage as ProductImageModel
from product.models import ProductOption as ProductOptionModel

""""""
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageModel
        fields = ["product", "image1", "image2", "image3", "image4", "image5"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = ProductModel
        fields = ["user", "title", "category", "thumbnail", "description", "view_count", "is_active", "is_delete",
                  "created_at", "updated_at"]
        extra_kwargs = {
            "is_delete": {"write_only": True}
        }