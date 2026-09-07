from django.views.generic import TemplateView

from careers.models import JobPosting
from quotes.forms import QuickQuoteForm
from stories.models import Story

from .models import FAQItem, Service


HOME_SERVICE_TILES = [
    ("images/serv5.jpg", "images/sv1.png", "Sea Transport",
     "Professional sea freight service delivering logistics solutions, optimizing every mile on every lane."),
    ("images/serv6.jpg", "images/sv2.png", "Road Freight",
     "Reliable road freight service delivering logistics solutions, optimizing every mile on every lane."),
    ("images/serv7.jpg", "images/sv3.png", "Air Express",
     "Fast air freight service delivering logistics solutions, optimizing every mile on every lane."),
    ("images/serv8.jpg", "images/sv4.png", "Railway Logistics",
     "Efficient rail freight service delivering logistics solutions, optimizing every mile on every lane."),
]


class HomeView(TemplateView):
    template_name = "pages/home.html"
    extra_context = {"show_header_top": True}

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["home_service_tiles"] = HOME_SERVICE_TILES
        ctx["stories"] = Story.objects.filter(is_approved=True).order_by("-created_at")[:6]
        ctx["quick_quote_form"] = QuickQuoteForm()
        ctx["open_roles_count"] = JobPosting.objects.filter(is_active=True).count()
        return ctx


TEAM_MEMBERS = [
    ("Jenny Noah", "Head of Operations", "images/tm1.jpg"),
    ("Jenny Mache", "Logistics Director", "images/tm2.jpg"),
    ("Sofia Melisa", "Project Manager", "images/tm3.jpg"),
    ("Shane Darren", "Supply Chain Lead", "images/tm4.jpg"),
]


class AboutView(TemplateView):
    template_name = "pages/about.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["team_members"] = TEAM_MEMBERS
        return ctx


SERVICE_PAGE_FAQS = [
    (
        "How can I track my shipment?",
        "You can easily track your shipment by entering your Tracking ID into our online "
        "tracking tool. Once submitted, you'll receive real-time updates on your shipment's "
        "location and delivery status.",
    ),
    (
        "How do I get in touch with customer support?",
        "Meeting project deadlines is a top priority. We understand the importance of timely "
        "delivery and have established a comprehensive approach to ensure all projects are "
        "completed on schedule.",
    ),
    (
        "What if my shipment is delayed or lost?",
        "We take full responsibility for delays or losses. Contact our support team "
        "immediately with your tracking ID and we will investigate and resolve the issue "
        "promptly.",
    ),
    (
        "Can I schedule recurring shipments?",
        "Yes! We offer flexible scheduling for recurring shipments. Contact us to set up a "
        "regular pickup and delivery plan tailored to your business needs.",
    ),
    (
        "What is your pricing model?",
        "Our pricing is based on shipment weight, dimensions, distance, and service type. Use "
        "our free instant quote calculator for a transparent estimate with no hidden fees.",
    ),
]


class ServicesView(TemplateView):
    template_name = "pages/services.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["services"] = Service.objects.filter(is_active=True)
        ctx["quick_quote_form"] = QuickQuoteForm()
        ctx["service_faqs"] = SERVICE_PAGE_FAQS
        return ctx


class FAQView(TemplateView):
    template_name = "pages/faq.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["faqs"] = FAQItem.objects.filter(is_active=True)
        return ctx


class PrivacyPolicyView(TemplateView):
    template_name = "pages/policy.html"
    extra_context = {"show_header_top": True}


class TermsView(TemplateView):
    template_name = "pages/terms.html"
    extra_context = {"show_header_top": True}


class SitemapPageView(TemplateView):
    template_name = "pages/sitemap.html"
