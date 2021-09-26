from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom user admin """

    list_display = ("username", "gender", "language", "superhost", "currency")

    # 우리가 슈퍼호스트인지 어드민페이지에서 알아보려면 리스트 필터 사용
    list_filter = ("superhost", "currency", "superhost")

    # 여기 fields  대문자 하기만해도 오류냠
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom field",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
