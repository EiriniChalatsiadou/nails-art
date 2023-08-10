from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Treatment, TreatmentType


# Create your views here.


class Treatments(TemplateView):
    """
    Homepage
    """

    template_name = "treatments.html"

    def get_context_data(self, **kwargs):
        context = super(Treatments, self).get_context_data(**kwargs)

        # get all treatments of specific type
        context['shellac'] = Treatment.objects.filter(treatmentType__name__contains="Shellac")
        context['gel_nails'] = Treatment.objects.filter(treatmentType__name__contains="Gel nails")
        context['manicure'] = Treatment.objects.filter(treatmentType__name__contains="Manicure")
        context['pedicure'] = Treatment.objects.filter(treatmentType__name__contains="Pedicure")

        return context
