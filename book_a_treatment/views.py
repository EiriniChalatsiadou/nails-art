from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class bookAtreatment(TemplateView):
    """
    Homepage
    """

    template_name = "book_a_treatment.html"