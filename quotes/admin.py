from django.contrib import admin

from .models import QuoteRequest


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = (
        "name", "email", "freight_type", "departure", "city_deliver",
        "weight", "price_low", "price_high", "source", "status", "created_at",
    )
    list_editable = ("status",)
    list_filter = ("status", "source", "freight_type", "created_at")
    search_fields = ("name", "email", "phone", "departure", "city_deliver")
    readonly_fields = ("created_at",)
