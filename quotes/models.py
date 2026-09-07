from django.db import models


class QuoteRequest(models.Model):
    FREIGHT_CHOICES = [
        ("Air Freight", "Air Freight"),
        ("Ocean Freight", "Ocean Freight"),
        ("Road Freight", "Road Freight"),
        ("Warehousing", "Warehousing"),
    ]
    INCOTERM_CHOICES = [
        ("EXW", "EXW"),
        ("FOB", "FOB"),
        ("CIF", "CIF"),
        ("DAP", "DAP"),
    ]
    STATUS_CHOICES = [
        ("new", "New"),
        ("contacted", "Contacted"),
        ("quoted", "Quoted"),
        ("closed", "Closed"),
    ]

    SOURCE_CHOICES = [
        ("quick", "Homepage quick quote"),
        ("full", "Quote page calculator"),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=40)

    freight_type = models.CharField(max_length=30)
    departure = models.CharField(max_length=120, blank=True)
    city_deliver = models.CharField(max_length=120)
    incoterms = models.CharField(max_length=10, choices=INCOTERM_CHOICES, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dimensions = models.CharField(max_length=80, blank=True)
    ship_date = models.CharField(max_length=40, blank=True)
    source = models.CharField(max_length=10, choices=SOURCE_CHOICES, default="full")

    price_low = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    price_high = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    transit_estimate = models.CharField(max_length=80, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.departure} to {self.city_deliver} ({self.freight_type})"
