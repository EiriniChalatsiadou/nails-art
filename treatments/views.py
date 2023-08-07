from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Treatments(TemplateView):
    """
    Homepage
    """

    template_name = "treatments.html"
