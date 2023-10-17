from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"

@user_passes_test(lambda u: u.is_authenticated, login_url='/pages/please_login/')
def calculator_view(request):
    return render(request, 'pages/calculator.html', {})