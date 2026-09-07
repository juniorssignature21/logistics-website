from django.db import models


class Shipment(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending Pickup"),
        ("in_transit", "In Transit"),
        ("customs", "Customs Clearance"),
        ("out_for_delivery", "Out for Delivery"),
        ("delivered", "Delivered"),
        ("exception", "Exception"),
    ]

    tracking_number = models.CharField(max_length=40, unique=True)
    sender_name = models.CharField(max_length=150, blank=True)
    receiver_name = models.CharField(max_length=150, blank=True)
    origin = models.CharField(max_length=150)
    destination = models.CharField(max_length=150)
    service_type = models.CharField(max_length=100, blank=True, default="Standard Freight")
    weight = models.CharField(max_length=40, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    estimated_delivery = models.DateField(null=True, blank=True)
    notify_email = models.EmailField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.tracking_number

    def get_status_display_icon(self):
        return {
            "pending": "bi-hourglass-split",
            "in_transit": "bi-truck",
            "customs": "bi-file-earmark-check",
            "out_for_delivery": "bi-geo-alt",
            "delivered": "bi-check-circle-fill",
            "exception": "bi-exclamation-triangle-fill",
        }.get(self.status, "bi-box-seam")

    @property
    def progress_percent(self):
        return {
            "pending": 10,
            "in_transit": 45,
            "customs": 60,
            "out_for_delivery": 85,
            "delivered": 100,
            "exception": 50,
        }.get(self.status, 10)

    @property
    def current_location(self):
        last_event = self.events.order_by("-timestamp").first()
        return last_event.location if last_event else self.origin


class ShipmentEvent(models.Model):
    shipment = models.ForeignKey(Shipment, related_name="events", on_delete=models.CASCADE)
    status = models.CharField(max_length=150)
    location = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=255, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return f"{self.shipment.tracking_number} — {self.status}"
