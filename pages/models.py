from django.db import models


class SiteSetting(models.Model):
    """Singleton-style model holding the contact/social details shown in the
    header, footer, and legal modals across the whole site."""

    site_name = models.CharField(max_length=120, default="Global Axis Cargo")
    tagline = models.CharField(max_length=200, blank=True, default="Transport & Logistics")

    phone = models.CharField(max_length=40, default="+1 234 567 890")
    phone_secondary = models.CharField(max_length=40, blank=True, default="+92 8208 383 727")
    email = models.EmailField(default="support@globalaxiscargo.com")
    address = models.CharField(max_length=255, default="123 Street, New York, USA")

    facebook_url = models.URLField(blank=True, default="https://facebook.com/GlobalAxisCargo")
    twitter_url = models.URLField(blank=True, default="https://twitter.com/GlobalAxisCargo")
    instagram_url = models.URLField(blank=True, default="https://instagram.com/GlobalAxisCargo")
    linkedin_url = models.URLField(blank=True, default="")
    youtube_url = models.URLField(blank=True, default="https://youtube.com/GlobalAxisCargo")
    whatsapp_number = models.CharField(max_length=40, blank=True, default="1234567890")
    telegram_username = models.CharField(max_length=80, blank=True, default="")

    shipping_policy_text = models.TextField(
        default=(
            "All shipments are processed and handled with the utmost care and professionalism. "
            "Delivery timelines are estimates and may vary due to customs, weather, or unforeseen "
            "logistical issues. The customer is responsible for providing accurate and complete "
            "recipient information. Packages returned due to incorrect addresses may incur "
            "additional shipping charges or redelivery fees. Our liability for loss or damage is "
            "limited to the declared value of the item, subject to our maximum insurance coverage."
        )
    )
    privacy_policy_text = models.TextField(
        default=(
            "We are committed to protecting your privacy. We collect data (names, addresses, "
            "contact numbers) solely for the purpose of processing, tracking, and delivering your "
            "shipments. We do not sell or rent your personal data for marketing purposes. All "
            "collected data is secured using industry-standard encryption."
        )
    )
    terms_text = models.TextField(
        default=(
            "By using our logistics and courier services, you agree to be bound by these Terms of "
            "Service and all applicable laws and regulations. The client is solely responsible for "
            "the accurate description and lawful contents of all packages. We reserve the right to "
            "inspect any shipment for security reasons."
        )
    )

    class Meta:
        verbose_name = "Site setting"
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.site_name

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Service(models.Model):
    """A logistics service offered, shown on the homepage and services page."""

    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, unique=True)
    icon = models.CharField(
        max_length=60,
        default="bi bi-box-seam",
        help_text="Bootstrap Icons class, e.g. 'bi bi-box-seam'",
    )
    short_description = models.CharField(max_length=280)
    description = models.TextField(blank=True)
    features_text = models.TextField(
        blank=True,
        help_text=(
            "One feature per line, formatted as 'bootstrap-icon-class|Feature text', "
            "e.g. 'bi bi-geo-alt-fill|Global Reach: 220+ Countries.'"
        ),
    )
    thumbnail_image = models.CharField(
        max_length=100,
        blank=True,
        help_text="Static image path for the card thumbnail, e.g. 'images/serv-s1.png'.",
    )
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    cta_label = models.CharField(max_length=60, default="Get a Quote")
    cta_url_name = models.CharField(
        max_length=60,
        default="quotes:page",
        help_text="Django url name the call-to-action button links to.",
    )
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    @property
    def features(self):
        result = []
        for line in self.features_text.splitlines():
            line = line.strip()
            if not line:
                continue
            icon, _, text = line.partition("|")
            result.append((icon.strip() or "bi bi-check-circle-fill", text.strip() or icon.strip()))
        return result


class FAQItem(models.Model):
    CATEGORY_CHOICES = [
        ("tracking", "Tracking & Delivery Status"),
        ("pricing", "Pricing, Customs & Duties"),
        ("insurance", "Insurance & Liability"),
        ("general", "General"),
    ]
    CATEGORY_ICONS = {
        "tracking": "bi bi-geo-alt-fill",
        "pricing": "bi bi-currency-dollar",
        "insurance": "bi bi-shield-check",
        "general": "bi bi-question-circle-fill",
    }

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="general")
    question = models.CharField(max_length=255)
    answer = models.TextField(help_text="Basic HTML (links, lists) is allowed and rendered as-is.")
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["category", "order", "id"]
        verbose_name = "FAQ item"
        verbose_name_plural = "FAQ items"

    def __str__(self):
        return self.question

    @property
    def category_icon(self):
        return self.CATEGORY_ICONS.get(self.category, "bi bi-question-circle-fill")
