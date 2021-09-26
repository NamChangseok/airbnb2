from django.contrib import admin
from django.contrib.admin.options import HORIZONTAL
from . import models


@admin.register(models.RoomType, models.Facility, models.Amenities, models.HouseRules)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "city")},
        ),
        (
            "Times",
            {
                "fields": (
                    "check_in",
                    "check_out",
                )
            },
        ),
        (
            "More About Spaces",
            {
                "fields": (
                    "amenities",
                    "facility",
                    "house_rules",
                )
            },
        ),
        (
            "Spaces",
            {
                "fields": (
                    "bath",
                    "guests",
                    "bedrooms",
                )
            },
        ),
        (
            "Last Detail",
            {
                "fields": (
                    "host",
                    "price",
                )
            },
        ),
    )

    list_display = (
        "name",
        "city",
        "check_in",
        "check_out",
        "count_amenities",
    )

    list_filter = (
        "instant_book",
        "host__superhost",
        "city",
        "facility",
        "room_type",
        "house_rules",
    )

    search_fields = ("^city", "bath", "^host__username")
    filter_horizontal = (
        "amenities",
        "facility",
        "house_rules",
    )

    def count_amenities(self, obj):
        return obj.amenities.count()

    count_amenities.short_description = "Count Ameneties"


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


# Register your models here.
