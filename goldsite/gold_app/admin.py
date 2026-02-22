from django.contrib import admin
from .models import *

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