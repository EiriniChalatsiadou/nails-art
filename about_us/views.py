from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class AboutUs(TemplateView):
    """
    Homepage
    """

    template_name = "about_us.html"