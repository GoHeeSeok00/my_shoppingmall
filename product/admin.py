from django.contrib import admin

from product.models import Product as ProductModel
from product.models import ProductImage as ProductImageModel
from product.models import ProductOption as ProductOptionModel
from product.models import Category as CategoryModel

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(ProductImageModel)
admin.site.register(ProductOptionModel)
admin.site.register(CategoryModel)