from django.contrib import admin
from .models import *
from django.utils.html import format_html

@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "request_type",
        "status",
        "created_at"
    )

    list_filter = ("request_type", "status", "created_at")
    search_fields = ("name", "email", "phone")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Customer Info", {"fields": ("name", "email", "phone")}),

        ("Request Details", {"fields": ("request_type", "message")}),

        ("System Status", {"fields": ("status",)}),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)

    ordering = ("-created_at",)
    readonly_fields = ("created_at",)



@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):

    list_display = ("name", "position", "display_image")
    search_fields = ("name", "position")

    def display_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="50" height="50" style="object-fit:cover; border-radius:5px;" />',
                obj.image.url
            )
        return "No Image"

    display_image.short_description = "Image"