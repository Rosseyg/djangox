from django.urls import path

from .views import HomePageView, AboutPageView, calculator_view

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("calculator/", calculator_view, name="calculator"),
]
