from django.contrib import admin

from .models import Shipment, ShipmentEvent


class ShipmentEventInline(admin.TabularInline):
    model = ShipmentEvent
    extra = 1


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = (
        "tracking_number", "origin", "destination", "status",
        "estimated_delivery", "updated_at",
    )
    list_filter = ("status",)
    search_fields = ("tracking_number", "sender_name", "receiver_name", "origin", "destination")
    inlines = [ShipmentEventInline]


@admin.register(ShipmentEvent)
class ShipmentEventAdmin(admin.ModelAdmin):
    list_display = ("shipment", "status", "location", "timestamp")
    list_filter = ("status",)
