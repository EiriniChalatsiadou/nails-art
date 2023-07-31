from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.


class Home(ListView):
    """
    Homepage
    """

    template_name = "index.html"

    def get_queryset(self):
        pass
