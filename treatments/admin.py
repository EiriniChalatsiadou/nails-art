from django.contrib import admin
from .models import TreatmentType, Treatment

# Register your models here.
admin.site.register(TreatmentType)
admin.site.register(Treatment)