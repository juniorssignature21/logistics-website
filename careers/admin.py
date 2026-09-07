from django.contrib import admin

from .models import JobApplication, JobPosting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "location", "order", "is_active", "created_at")
    list_editable = ("order", "is_active")
    search_fields = ("title", "department", "location")


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "job_title", "location", "is_reviewed", "created_at")
    list_editable = ("is_reviewed",)
    list_filter = ("is_reviewed", "created_at")
    search_fields = ("full_name", "email", "job_title")
    readonly_fields = ("created_at",)
