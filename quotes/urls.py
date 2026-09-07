from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path("", views.QuotePageView.as_view(), name="page"),
    path("calculate/", views.QuoteCalculateView.as_view(), name="calculate"),
    path("quick/", views.QuickQuoteSubmitView.as_view(), name="quick_submit"),
]
