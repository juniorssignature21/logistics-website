from django.db import models


class JobPosting(models.Model):
    title = models.CharField(max_length=150)
    department = models.CharField(max_length=120)
    location = models.CharField(max_length=150)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["order", "-created_at"]

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    job_title = models.CharField(
        max_length=150,
        default="General Application",
        help_text="Free-text role applied for (matches the job posting title, or 'General Application').",
    )
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=150, blank=True)
    resume = models.FileField(upload_to="resumes/%Y/%m/")
    message = models.TextField(blank=True)
    agreed_privacy = models.BooleanField(default=False)

    is_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.full_name} — {self.job_title}"
