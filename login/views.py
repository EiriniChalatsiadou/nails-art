from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class Login(TemplateView):
    """
    Homepage
    """

    template_name = "login.html"