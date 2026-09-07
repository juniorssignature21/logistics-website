from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "inquiry_type", "urgency", "is_read", "created_at")
    list_editable = ("is_read",)
    list_filter = ("inquiry_type", "urgency", "is_read", "created_at")
    search_fields = ("name", "email", "phone", "subject", "message")
    readonly_fields = ("created_at",)
