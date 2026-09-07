import json

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView

from .forms import QuickQuoteForm, QuoteForm
from .pricing import calculate_quote


class QuotePageView(TemplateView):
    template_name = "quotes/quote.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["form"] = QuoteForm()
        return ctx


class QuoteCalculateView(View):
    """AJAX endpoint used by the quote page's "Calculate Quote" button.

    Mirrors the original template's process_quote.php JSON contract:
    {success, route, freight_type, price_low, price_high, transit, breakdown, note}
    """

    def post(self, request, *args, **kwargs):
        form = QuoteForm(request.POST)
        if not form.is_valid():
            first_error = next(iter(form.errors.values()))[0]
            return JsonResponse({"success": False, "message": first_error}, status=400)

        quote_request = form.save(commit=False)
        quote_request.source = "full"

        result = calculate_quote(
            freight_type=quote_request.freight_type,
            weight=quote_request.weight,
            departure=quote_request.departure,
            destination=quote_request.city_deliver,
        )
        quote_request.price_low = result["price_low"]
        quote_request.price_high = result["price_high"]
        quote_request.transit_estimate = result["transit"]
        quote_request.save()

        return JsonResponse({"success": True, **result})


class QuickQuoteSubmitView(View):
    """Handles the "Request Quote Form" widget embedded on the homepage."""

    def post(self, request, *args, **kwargs):
        form = QuickQuoteForm(request.POST)
        if form.is_valid():
            quote_request = form.save(commit=False)
            quote_request.source = "quick"
            result = calculate_quote(
                freight_type=quote_request.freight_type or "General Cargo",
                weight=quote_request.weight,
                departure="",
                destination=quote_request.city_deliver,
            )
            quote_request.price_low = result["price_low"]
            quote_request.price_high = result["price_high"]
            quote_request.transit_estimate = result["transit"]
            quote_request.save()

            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"success": True, **result})
            messages.success(
                request,
                "Thanks! Your quote request has been received — our team will reach out shortly.",
            )
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                first_error = next(iter(form.errors.values()))[0]
                return JsonResponse({"success": False, "message": first_error}, status=400)
            messages.error(request, "Please check the form and try again.")

        return redirect(request.META.get("HTTP_REFERER", "/") + "#request-quote")
