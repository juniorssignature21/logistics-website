from django.db import models


class Story(models.Model):
    SERVICE_CHOICES = [
        ("express", "Express International"),
        ("standard", "Standard Freight"),
        ("domestic", "Domestic Next-Day"),
    ]
    LANGUAGE_CHOICES = [
        ("en", "English"),
        ("es", "Spanish (Español)"),
        ("fr", "French (Français)"),
        ("de", "German (Deutsch)"),
        ("pt", "Portuguese (Português)"),
        ("ar", "Arabic (العربية)"),
        ("zh", "Chinese (简体中文)"),
        ("ru", "Russian (Русский)"),
        ("hi", "Hindi (हिन्दी)"),
    ]
    RATING_CHOICES = [(i, str(i)) for i in range(1, 6)]

    client_name = models.CharField(max_length=150)
    client_location = models.CharField(max_length=150)
    product_service = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    testimonial = models.TextField(max_length=500)
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default="en")
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES, default=5)
    profile_image = models.ImageField(upload_to="stories/", blank=True, null=True)

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Stories"

    def __str__(self):
        return f"{self.client_name} ({self.rating}★)"
