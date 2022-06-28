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
    category = CategorySerializer(many=True)
    productimage_set = ProductImageSerializer(many=True)
    productoption_set = ProductOptionSerializer(many=True, required=False)

    class Meta:
        model = ProductModel
        fields = ["user", "title", "category", "thumbnail", "description", "view_count", "is_active", "is_delete",
                  "created_at", "updated_at", "productimage_set", "productoption_set"]
        extra_kwargs = {
            "is_delete": {"write_only": True}
        }