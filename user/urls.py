from django.urls import path
from user.views import UserApiView, LoginApiView, LogoutApiView, UserDetailApiView, UserAddressApiView

app_name = "user"

urlpatterns = [
    path('', UserApiView.as_view(), name='user'),  # class엔 as_view()를 붙여주어야 한다.
    path('login/', LoginApiView.as_view(), name='login'),
    path('logout/', LogoutApiView.as_view(), name='logout'),
    path('address/', UserAddressApiView.as_view(), name='user_address'),
    path('address/<obj_id>/', UserAddressApiView.as_view(), name='user_address'),
    path('<obj_id>/', UserDetailApiView.as_view(), name='user_detail'),
]