from django.db import migrations

SERVICES = [
    {
        "title": "International Priority Express",
        "slug": "international-priority-express",
        "icon": "bi bi-box-seam",
        "short_description": "Time-critical documents and e-commerce, delivered door-to-door in 1-3 days.",
        "thumbnail_image": "images/serv-s1.png",
        "cta_label": "Get Express Quote",
        "cta_url_name": "quotes:page",
        "order": 1,
        "features_text": (
            "bi bi-geo-alt-fill|Global Reach: 220+ Countries.\n"
            "bi bi-clock-fill|Speed: 1-3 Business Days Guaranteed.\n"
            "bi bi-shield-fill-check|Ideal For: Urgent documents and time-critical e-commerce.\n"
            "bi bi-truck|Features: Door-to-door, live tracking, customs clearance."
        ),
    },
    {
        "title": "Air & Sea Freight Logistics",
        "slug": "air-sea-freight-logistics",
        "icon": "bi bi-box-seam",
        "short_description": "Heavy, LCL/FCL, and pallet shipments with the best value transit times.",
        "thumbnail_image": "images/serv-s2.png",
        "cta_label": "Request Freight Pricing",
        "cta_url_name": "quotes:page",
        "order": 2,
        "features_text": (
            "bi bi-box-seam-fill|Volume: Heavy, LCL/FCL, and Pallet Shipments.\n"
            "bi bi-clock-fill|Speed: 5-15 Business Days (Best Value).\n"
            "bi bi-truck-flatbed|Ideal For: Commercial inventory and bulk trade.\n"
            "bi bi-list-columns-reverse|Features: Customs brokerage, secure warehousing."
        ),
    },
    {
        "title": "Domestic & Ground Shipping",
        "slug": "domestic-ground-shipping",
        "icon": "bi bi-box-seam",
        "short_description": "Same-day to next-day delivery for local B2B transfers and fulfillment.",
        "thumbnail_image": "images/serv-s3.png",
        "cta_label": "Book Local Delivery",
        "cta_url_name": "quotes:page",
        "order": 3,
        "features_text": (
            "bi bi-house-door-fill|Local Focus: Fast service within your regional hub.\n"
            "bi bi-clock-fill|Speed: Same-Day to Next-Day Delivery.\n"
            "bi bi-shop|Ideal For: Local B2B transfers and e-commerce fulfillment.\n"
            "bi bi-map|Features: Flexible scheduling and instant POD."
        ),
    },
    {
        "title": "Cold Chain & Medical Logistics",
        "slug": "cold-chain-medical-logistics",
        "icon": "bi bi-box-seam",
        "short_description": "Temperature-controlled transport for vaccines, organs, and lab samples.",
        "thumbnail_image": "images/serv-s4.png",
        "cta_label": "Consult Experts",
        "cta_url_name": "contact:page",
        "order": 4,
        "features_text": (
            "bi bi-thermometer-half|Control: Temperature-controlled containers.\n"
            "bi bi-hospital|Compliance: Full regulatory compliance (GDP, GAMP).\n"
            "bi bi-bandaid-fill|Ideal For: Vaccines, organs, lab samples.\n"
            "bi bi-alarm-fill|Features: Real-time temp monitoring, emergency teams."
        ),
    },
    {
        "title": "E-commerce Fulfillment & 3PL",
        "slug": "ecommerce-fulfillment-3pl",
        "icon": "bi bi-box-seam",
        "short_description": "Inventory warehousing, pick-pack-ship, and API integration for online stores.",
        "thumbnail_image": "images/serv-s5.png",
        "cta_label": "View 3PL Solutions",
        "cta_url_name": "contact:page",
        "order": 5,
        "features_text": (
            "bi bi-boxes|Storage: Inventory warehousing (Pick, Pack, Ship).\n"
            "bi bi-link-45deg|Integration: Seamless API integration with major platforms.\n"
            "bi bi-currency-dollar|Ideal For: Scaling online stores and dropshipping.\n"
            "bi bi-arrow-return-left|Features: Returns processing, custom packaging."
        ),
    },
    {
        "title": "Customs Brokerage & Consulting",
        "slug": "customs-brokerage-consulting",
        "icon": "bi bi-box-seam",
        "short_description": "Licensed customs brokers to help you avoid delays and complex regulations.",
        "thumbnail_image": "images/serv-s6.png",
        "cta_label": "Simplify Customs",
        "cta_url_name": "contact:page",
        "order": 6,
        "features_text": (
            "bi bi-file-earmark-check-fill|Expertise: Dedicated licensed customs brokers.\n"
            "bi bi-globe2|Compliance: Duties, taxes, tariffs, and declarations.\n"
            "bi bi-x-octagon-fill|Ideal For: Avoiding delays and complex regulations.\n"
            "bi bi-book|Features: HS classification, import/export permits."
        ),
    },
    {
        "title": "Heavy & Specialized Transport",
        "slug": "heavy-specialized-transport",
        "icon": "bi bi-box-seam",
        "short_description": "Oversized, odd-dimension, and project cargo with full route planning.",
        "thumbnail_image": "images/serv5.jpg",
        "cta_label": "Plan Your Project",
        "cta_url_name": "contact:page",
        "order": 7,
        "features_text": (
            "bi bi-toggles|Handling: Oversized, odd-dimension, and project cargo.\n"
            "bi bi-sign-turn-right-fill|Planning: Route surveys, permitting, and police escorts.\n"
            "bi bi-tools|Ideal For: Construction machinery, oil/gas equipment.\n"
            "bi bi-shield-lock-fill|Features: Specialized rigging, lifting, insurance."
        ),
    },
    {
        "title": "White Glove & Final Mile",
        "slug": "white-glove-final-mile",
        "icon": "bi bi-box-seam",
        "short_description": "Dedicated personnel for premium handling of luxury goods and fine art.",
        "thumbnail_image": "images/serv6.jpg",
        "cta_label": "Book Premium Service",
        "cta_url_name": "quotes:page",
        "order": 8,
        "features_text": (
            "bi bi-person-fill|Service: Dedicated personnel for premium handling.\n"
            "bi bi-wrench-adjustable-fill|Value-Add: Inside delivery, assembly, debris removal.\n"
            "bi bi-house-fill|Ideal For: Luxury goods, fine art, and furniture.\n"
            "bi bi-calendar-check|Features: Appointment scheduling, signature confirmation."
        ),
    },
    {
        "title": "Secure Document & Banking Runs",
        "slug": "secure-document-banking-runs",
        "icon": "bi bi-box-seam",
        "short_description": "Dedicated, non-stop, secure transport for legal and banking documents.",
        "thumbnail_image": "images/serv7.jpg",
        "cta_label": "Arrange Secure Pickup",
        "cta_url_name": "contact:page",
        "order": 9,
        "features_text": (
            "bi bi-file-lock2-fill|Security: Dedicated, non-stop, secure transport.\n"
            "bi bi-fingerprint|Verification: Chain of custody and signature capture.\n"
            "bi bi-bank|Ideal For: Legal contracts, banking deposits, passports.\n"
            "bi bi-geo-alt-fill|Features: GPS-enabled couriers, scheduled routes."
        ),
    },
]

FAQS = [
    ("tracking", "Where can I track my shipment?",
     "You can track your shipment instantly on our dedicated <a href=\"/track/\">Tracking Page</a>. "
     "Simply enter your Tracking Number in the provided field. Please allow up to 4 hours after "
     "receiving your confirmation email for the tracking information to become live in our system.", 1),
    ("tracking", "Why hasn't my tracking status updated?",
     "Tracking updates typically occur when a parcel is scanned at major transit points. If the status "
     "has stalled for more than 24 hours for Express shipments or 3 business days for Freight, it may be "
     "currently undergoing Customs Clearance, or on a long-haul flight or sea route where intermediate "
     "scans are limited. If the delay exceeds these periods, please contact our support team with your "
     "tracking number.", 2),
    ("tracking", "What happens if I missed my delivery attempt?",
     "Our couriers typically attempt delivery twice. After the first failed attempt, they will leave a "
     "notification card (or send an email/SMS) with instructions on how to reschedule a delivery or where "
     "to pick up the package at a local depot. If both attempts fail, the package may be held for a short "
     "period before being returned to the sender.", 3),
    ("pricing", "What is the difference between DDU and DDP?",
     "These are Incoterms defining responsibility for duties and taxes: <strong>DDU (Delivered Duty "
     "Unpaid)</strong> — the recipient is responsible for paying any import duties, taxes, and customs "
     "fees upon arrival. <strong>DDP (Delivered Duty Paid)</strong> — the sender pays all duties, taxes, "
     "and customs fees upfront at the time of booking.", 1),
    ("pricing", "How are shipping costs calculated?",
     "Costs are calculated based on the greater of two measures: Actual Weight or Volumetric Weight "
     "(Dimensional Weight). Volumetric Weight is calculated using the formula: (Length × Width × "
     "Height) / Divisor. You can use our <a href=\"/quote/\">Quote Calculator</a> for a precise estimate.", 2),
    ("pricing", "My package is held by customs. What should I do?",
     "Customs holds are usually due to missing documentation or outstanding duties/taxes. Check your "
     "tracking details for a specific notification. If you require assistance, our dedicated Customs "
     "Brokerage Team can help expedite the release. <a href=\"/contact/\">Contact us for expert support</a>.", 3),
    ("insurance", "Is my shipment automatically insured?",
     "All shipments include a basic level of carrier liability coverage. For high-value goods, we highly "
     "recommend purchasing All-Risk Shipment Insurance during the booking process. This provides "
     "comprehensive coverage up to the full declared commercial value against loss or damage.", 1),
    ("insurance", "How do I file a claim for loss or damage?",
     "Claims must be filed by the shipper within 7 calendar days of delivery (for visible damage) or 30 "
     "days of the expected delivery date (for loss). Required documents: tracking number, proof of "
     "commercial value (invoice), and photographic evidence (for damage claims).", 2),
]


def seed_data(apps, schema_editor):
    Service = apps.get_model("pages", "Service")
    FAQItem = apps.get_model("pages", "FAQItem")

    for data in SERVICES:
        Service.objects.get_or_create(slug=data["slug"], defaults=data)

    for category, question, answer, order in FAQS:
        FAQItem.objects.get_or_create(
            question=question,
            defaults={"category": category, "answer": answer, "order": order},
        )


def remove_data(apps, schema_editor):
    Service = apps.get_model("pages", "Service")
    FAQItem = apps.get_model("pages", "FAQItem")
    Service.objects.filter(slug__in=[d["slug"] for d in SERVICES]).delete()
    FAQItem.objects.filter(question__in=[q for _, q, _, _ in FAQS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, remove_data),
    ]
