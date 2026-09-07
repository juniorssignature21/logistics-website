from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import ContactForm


class ContactPageView(TemplateView):
    template_name = "contact/contact.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = ContactForm()
        return ctx


class ContactSubmitView(View):
    """Endpoint backing the contact form (and the services-page appointment
    mini-form), replacing process_contact.php. Supports AJAX (JSON) and a
    plain POST fallback that redirects back with a flash message."""

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        is_ajax = request.headers.get("x-requested-with") == "XMLHttpRequest"

        if form.is_valid():
            form.save()
            message = "Your message has been received. Our team will get back to you shortly."
            if is_ajax:
                return JsonResponse({"success": True, "message": message})
            messages.success(request, message)
        else:
            first_error = next(iter(form.errors.values()))[0]
            if is_ajax:
                return JsonResponse({"success": False, "message": first_error}, status=400)
            messages.error(request, first_error)

        return redirect(request.META.get("HTTP_REFERER", "/"))
