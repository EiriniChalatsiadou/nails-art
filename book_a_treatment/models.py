from django.db import models
from django.conf import settings
from treatments import models as treatmentModels

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

class Booking(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    treatment = models.ForeignKey(treatmentModels.Treatment, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False, blank=False) 


