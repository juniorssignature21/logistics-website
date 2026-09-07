from django import forms
from django.core.exceptions import ValidationError

from .models import JobApplication

ALLOWED_RESUME_EXTENSIONS = (".pdf", ".doc", ".docx")
MAX_RESUME_SIZE_BYTES = 5 * 1024 * 1024


class JobApplicationForm(forms.ModelForm):
    agreed_privacy = forms.BooleanField(
        required=True,
        error_messages={"required": "Please confirm you agree to the Privacy Policy."},
    )

    class Meta:
        model = JobApplication
        fields = [
            "job_title", "full_name", "email", "phone", "location",
            "resume", "message", "agreed_privacy",
        ]

    def clean_resume(self):
        resume = self.cleaned_data["resume"]
        name = resume.name.lower()
        if not name.endswith(ALLOWED_RESUME_EXTENSIONS):
            raise ValidationError("Resume must be a PDF, DOC, or DOCX file.")
        if resume.size > MAX_RESUME_SIZE_BYTES:
            raise ValidationError("Resume file is too large. Max size is 5MB.")
        return resume
