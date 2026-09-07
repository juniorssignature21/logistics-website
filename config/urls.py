from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from pages import views as pages_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", pages_views.HomeView.as_view(), name="home"),
    path("about/", pages_views.AboutView.as_view(), name="about"),
    path("services/", pages_views.ServicesView.as_view(), name="services"),
    path("faq/", pages_views.FAQView.as_view(), name="faq"),
    path("privacy-policy/", pages_views.PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("terms-and-conditions/", pages_views.TermsView.as_view(), name="terms"),
    path("sitemap/", pages_views.SitemapPageView.as_view(), name="sitemap_page"),
    path("contact/", include("contact.urls")),
    path("quote/", include("quotes.urls")),
    path("careers/", include("careers.urls")),
    path("track/", include("tracking.urls")),
    path("stories/", include("stories.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / "static")
