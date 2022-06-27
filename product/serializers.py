from rest_framework import serializers

from product.models import Product as ProductModel

""""""
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ["user", "title", "category", "thumbnail", "description", "view_count", "is_active", "is_delete",
                  "created_at", "updated_at"]
        extra_kwargs = {
            "is_delete": {"write_only": True}
        }