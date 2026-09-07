from django.contrib import admin

from .models import Story


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ("client_name", "client_location", "product_service", "rating", "is_approved", "created_at")
    list_editable = ("is_approved",)
    list_filter = ("is_approved", "product_service", "rating")
    search_fields = ("client_name", "client_location", "testimonial")
