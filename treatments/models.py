from django.db import models

# Create your models here.

class TreatmentType(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

class Treatment(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.FloatField(null=False, blank=False, default=0.0)
    treatmentType = models.ForeignKey(TreatmentType, on_delete=models.CASCADE)



