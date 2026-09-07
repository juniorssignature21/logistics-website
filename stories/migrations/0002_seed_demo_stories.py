from django.db import migrations

STORIES = [
    ("Test User", "Nugeris", "domestic", "It was amazing, I think I love it — fast, careful, and the tracking was spot on.", 4),
    ("Test User", "Nugeris", "standard", "I really loved it, the delivery was smooth and well communicated throughout.", 4),
    (
        "Hudson & Wells Law", "New York, NY", "express",
        "For high-stakes contracts, discretion and speed are essential. Their dedicated messenger "
        "service provides an auditable, secure chain of custody every time.", 5,
    ),
]


def seed_data(apps, schema_editor):
    Story = apps.get_model("stories", "Story")
    for name, location, service, testimonial, rating in STORIES:
        Story.objects.get_or_create(
            client_name=name,
            testimonial=testimonial,
            defaults={
                "client_location": location,
                "product_service": service,
                "rating": rating,
                "language": "en",
                "is_approved": True,
            },
        )


def remove_data(apps, schema_editor):
    Story = apps.get_model("stories", "Story")
    Story.objects.filter(testimonial__in=[t for _, _, _, t, _ in STORIES]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("stories", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
