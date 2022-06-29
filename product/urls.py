from django.urls import path

from product.views import ProductApiView, ProductDetailApiView, ProductImageApiView

app_name = "product"

urlpatterns = [
    path('', ProductApiView.as_view(), name='product'),  # class엔 as_view()를 붙여주어야 한다.
    path('image/<obj_id>/', ProductImageApiView.as_view(), name='product_image'),
    path('<obj_id>/', ProductDetailApiView.as_view(), name='product_detail'),
    path('<obj_id>/image/', ProductImageApiView.as_view(), name='product_image'),
]