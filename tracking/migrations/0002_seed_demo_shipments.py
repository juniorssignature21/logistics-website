import datetime

from django.db import migrations
from django.utils import timezone


def seed_data(apps, schema_editor):
    Shipment = apps.get_model("tracking", "Shipment")
    ShipmentEvent = apps.get_model("tracking", "ShipmentEvent")
    now = timezone.now()

    shipment1, created = Shipment.objects.get_or_create(
        tracking_number="AWB-8F9C9B9E",
        defaults={
            "sender_name": "Global Axis Cargo Warehouse",
            "receiver_name": "Amara Okafor",
            "origin": "Lagos, Nigeria",
            "destination": "London, United Kingdom",
            "service_type": "International Priority Express",
            "weight": "4.2 kg",
            "status": "in_transit",
            "estimated_delivery": (now + datetime.timedelta(days=2)).date(),
        },
    )
    if created:
        events = [
            ("Shipment Booked", "Lagos, Nigeria", "Package received at origin facility.", 6.5244, 3.3792, now - datetime.timedelta(days=3)),
            ("Departed Origin Facility", "Lagos, Nigeria", "Handed off to international carrier.", 6.5244, 3.3792, now - datetime.timedelta(days=2, hours=18)),
            ("Customs Clearance", "Lagos, Nigeria", "Cleared export customs.", 6.5244, 3.3792, now - datetime.timedelta(days=2, hours=10)),
            ("In Transit", "Amsterdam, Netherlands", "Arrived at international transit hub.", 52.3676, 4.9041, now - datetime.timedelta(days=1, hours=6)),
            ("In Transit", "London, United Kingdom", "Arrived in destination country.", 51.5072, -0.1276, now - datetime.timedelta(hours=8)),
        ]
        for status, location, description, lat, lng, ts in events:
            ShipmentEvent.objects.create(
                shipment=shipment1, status=status, location=location,
                description=description, latitude=lat, longitude=lng, timestamp=ts,
            )

    shipment2, created2 = Shipment.objects.get_or_create(
        tracking_number="AWB-3D7A1C22",
        defaults={
            "sender_name": "Hudson & Wells Law",
            "receiver_name": "First National Trust",
            "origin": "New York, NY, USA",
            "destination": "New York, NY, USA",
            "service_type": "Secure Document & Banking Runs",
            "weight": "0.3 kg",
            "status": "delivered",
            "estimated_delivery": (now - datetime.timedelta(days=1)).date(),
        },
    )
    if created2:
        events2 = [
            ("Courier Dispatched", "New York, NY, USA", "Secure courier assigned and dispatched.", 40.7128, -74.0060, now - datetime.timedelta(days=1, hours=3)),
            ("Delivered", "New York, NY, USA", "Signed for by recipient. Chain of custody complete.", 40.7484, -73.9857, now - datetime.timedelta(days=1, hours=1)),
        ]
        for status, location, description, lat, lng, ts in events2:
            ShipmentEvent.objects.create(
                shipment=shipment2, status=status, location=location,
                description=description, latitude=lat, longitude=lng, timestamp=ts,
            )


def remove_data(apps, schema_editor):
    Shipment = apps.get_model("tracking", "Shipment")
    Shipment.objects.filter(tracking_number__in=["AWB-8F9C9B9E", "AWB-3D7A1C22"]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("tracking", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
