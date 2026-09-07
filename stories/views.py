from django.contrib import messages
from django.shortcuts import redirect
from django.views import View

from .forms import StoryForm


class StorySubmitView(View):
    """Handles the homepage "Share Your Story" form (replaces index.php#entry)."""

    def post(self, request, *args, **kwargs):
        form = StoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for sharing your story! It will appear on the site once reviewed.",
            )
        else:
            messages.error(request, "Please check the story form and try again.")
        return redirect(request.META.get("HTTP_REFERER", "/") + "#entry")
