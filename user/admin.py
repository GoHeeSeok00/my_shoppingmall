from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from user.forms import CustomUserCreationForm, CustomUserChangeForm
from user.models import User as UserModel
from user.models import UserAddress as UserAddressModel

""""""
class CustomUserAdmin(BaseUserAdmin):
    model = UserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ("id", "profile_image", "username", "name", "is_seller", "is_active", "last_login")
    list_display_links = ("id", "username")
    # is_seller = T, is_active = F, last_login = nodata 필터  => 관리자 승인을 기다리는 판매자 회원 가입
    list_filter = ("is_seller", "is_active", "last_login")
    search_fields = ("username", "name")
    readonly_fields = ("join_date",)

    fieldsets = (
        ("info", {"fields": ("username", "password", "profile_image", "email", "name", "gender", "date_of_birth",
                             "mobile_number", "introduce", "join_date", "is_secession")}),
        ("Agreement", {"fields": ("is_terms_of_service", "is_privacy_policy", "is_receive_marketing_info")}),
        ("permissions", {"fields": ("is_admin", "is_seller", "is_active")})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("username",  "password1", "password2", "name", "email", "gender", "date_of_birth",
                       "mobile_number", "introduce", "is_seller", "is_terms_of_service", "is_privacy_policy",
                       "is_receive_marketing_info")}
         ),
    )

    filter_horizontal = []


# Unregister(Group)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(UserModel, CustomUserAdmin)
admin.site.register(UserAddressModel)