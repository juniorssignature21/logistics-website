from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import JobApplicationForm
from .models import JobPosting


class CareersPageView(TemplateView):
    template_name = "careers/careers.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["jobs"] = JobPosting.objects.filter(is_active=True)
        ctx["application_form"] = JobApplicationForm()
        return ctx


class ApplyView(View):
    """Handles the application modal form, replacing careers.php."""

    def post(self, request, *args, **kwargs):
        form = JobApplicationForm(request.POST, request.FILES)
        is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"

        if form.is_valid():
            form.save()
            if is_ajax:
                return JsonResponse(
                    {"success": True, "message": "Application submitted! We'll be in touch soon."}
                )
            messages.success(request, "Application submitted! We'll be in touch soon.")
        else:
            if is_ajax:
                first_error = next(iter(form.errors.values()))[0]
                return JsonResponse({"success": False, "message": first_error}, status=400)
            messages.error(request, "Please check the application form and try again.")

        return redirect("careers:page")
