from django import forms

from .models import Story


class StoryForm(forms.ModelForm):
    testimonial = forms.CharField(
        widget=forms.Textarea, min_length=20, max_length=500,
        error_messages={
            "min_length": "Please share your story (min 20, max 500 characters).",
        },
    )
    client_name = forms.CharField(min_length=2)

    class Meta:
        model = Story
        fields = [
            "client_name", "client_location", "product_service",
            "testimonial", "language", "rating", "profile_image",
        ]
