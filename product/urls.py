from django.urls import path

from product.views import ProductApiView, ProductDetailApiView

app_name = "product"

urlpatterns = [
    path('', ProductApiView.as_view(), name='product'),  # class엔 as_view()를 붙여주어야 한다.
    path('<obj_id>/', ProductDetailApiView.as_view(), name='product_detail'),
]