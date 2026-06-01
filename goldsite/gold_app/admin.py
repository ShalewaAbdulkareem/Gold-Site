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


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')

admin.site.register(Product, ProductAdmin)



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

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")
    search_fields = ("question",)



class CSRProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title', 'created_at')


admin.site.register(CSRProject, CSRProjectAdmin)
admin.site.register(CSRCategory)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = ('name', 'profession', 'created_at')



@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "preview",
        "created_at",
    )

    list_filter = (
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "category",
    )

    readonly_fields = (
        "preview",
        "created_at",
    )

    fieldsets = (
        ("Gallery Information", {
            "fields": (
                "title",
                "category",
                "image",
                "preview",
            )
        }),

        ("Dates", {
            "fields": (
                "created_at",
            )
        }),
    )

    def preview(self, obj):

        if obj.image:
            return format_html(
                '<img src="{}" width="120" '
                'style="border-radius:8px; object-fit:cover;" />',
                obj.image.url
            )

        return "No Image"

    preview.short_description = "Image Preview"    



@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "preview",
        "created_at",
    )

    search_fields = ("title",)

    def preview(self, obj):

        if obj.thumbnail:
            return format_html(
                '<img src="{}" width="100" style="border-radius:8px;" />',
                obj.thumbnail.url
            )

        return "No Thumbnail"

    preview.short_description = "Thumbnail"

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):

    list_display = ("title", "location", "duration","price","featured", "created_at") 

    list_filter = (
        "featured",
        "location",
    )

    search_fields = (
        "title",
        "location",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }