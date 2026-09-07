from django.db import migrations

JOBS = [
    ("Operations Coordinator", "Express Services", "New York, NY (Hybrid)",
     "Manage daily courier routing, optimize manifest creation, and liaise between drivers and "
     "customers to ensure service delivery targets are met.", 1),
    ("Commercial Truck Driver (CDL)", "Freight Transport", "Los Angeles, CA (Full-Time)",
     "Responsible for safe, on-time movement of LTL and FCL freight. Requires valid CDL and clean "
     "driving record.", 2),
    ("Customs Brokerage Specialist", "Global Trade", "Remote (Full-Time)",
     "Ensure compliance with international trade regulations, process duties/taxes, and manage "
     "complex import/export documentation.", 3),
    ("Warehouse Operations Manager", "Warehousing", "Chicago, IL (On-Site)",
     "Oversee inventory management, staff scheduling, and facility operations. Ensure safety "
     "compliance and operational efficiency.", 4),
    ("Supply Chain Analyst", "Analytics", "London, UK (Hybrid)",
     "Analyze logistics data, forecast demand, and optimize routing. Proficiency in SQL and data "
     "visualization tools required.", 5),
    ("Customer Success Manager", "Customer Experience", "Singapore (Full-Time)",
     "Build and maintain enterprise client relationships. Handle escalations and drive retention "
     "across APAC region accounts.", 6),
]


def seed_data(apps, schema_editor):
    JobPosting = apps.get_model("careers", "JobPosting")
    for title, department, location, description, order in JOBS:
        JobPosting.objects.get_or_create(
            title=title,
            defaults={
                "department": department,
                "location": location,
                "description": description,
                "order": order,
            },
        )


def remove_data(apps, schema_editor):
    JobPosting = apps.get_model("careers", "JobPosting")
    JobPosting.objects.filter(title__in=[title for title, *_ in JOBS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("careers", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
