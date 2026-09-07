from django.urls import path

from . import views

app_name = "stories"

urlpatterns = [
    path("submit/", views.StorySubmitView.as_view(), name="submit"),
]
