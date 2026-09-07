from django.urls import path

from . import views

app_name = "careers"

urlpatterns = [
    path("", views.CareersPageView.as_view(), name="page"),
    path("apply/", views.ApplyView.as_view(), name="apply"),
]
