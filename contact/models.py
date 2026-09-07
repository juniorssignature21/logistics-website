from django.db import models


class ContactMessage(models.Model):
    INQUIRY_CHOICES = [
        ("International Priority Express", "International Priority Express"),
        ("Air & Sea Freight", "Air & Sea Freight"),
        ("Domestic Shipping", "Domestic Shipping"),
        ("Cold Chain Logistics", "Cold Chain Logistics"),
        ("E-commerce 3PL", "E-commerce 3PL"),
        ("Customs Brokerage", "Customs Brokerage"),
        ("Heavy Transport", "Heavy Transport"),
        ("White Glove Delivery", "White Glove Delivery"),
        ("Secure Documents", "Secure Documents"),
        ("General Inquiry", "General Inquiry"),
    ]
    URGENCY_CHOICES = [
        ("Standard", "Standard"),
        ("Express", "Express"),
        ("Urgent", "Urgent"),
    ]

    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=40)
    inquiry_type = models.CharField(max_length=60, choices=INQUIRY_CHOICES)
    urgency = models.CharField(max_length=20, choices=URGENCY_CHOICES)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} — {self.subject}"
