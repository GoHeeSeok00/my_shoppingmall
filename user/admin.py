from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from user.models import User as UserModel
from user.models import UserAddress as UserAddressModel

""""""
class CustomUserAdmin(BaseUserAdmin):
    model = UserModel
    ordering = ('userid',)

    list_display = ("id", "userid", "name")
    list_display_links = ("id", "userid")
    list_filter = ("userid", "name")
    search_fields = ("userid", "name")
    readonly_fields = ("userid", "join_date")

    fieldsets = (
        ("info", {"fields": ("userid", "password", "email", "name", "gender", "date_of_birth", "mobile_number",
                             "introduce", "join_date", "is_secession")}),
        ("Agreement", {"fields": ("is_terms_of_service", "is_privacy_policy", "is_receive_marketing_info")}),
        ("permissions", {"fields": ("is_admin", "is_seller", "is_active")})
    )

    filter_horizontal = []


# Unregister(Group)
admin.site.unregister(Group)

# Register your models here.
admin.site.register(UserModel, CustomUserAdmin)
admin.site.register(UserAddressModel)