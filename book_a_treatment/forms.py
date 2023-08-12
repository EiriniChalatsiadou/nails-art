from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [ 'treatment', 'staff', 'date']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'float-end'}, format='%Y-%m-%dT%H:%M'),
            'treatment': forms.Select(attrs={'class': 'float-end'}),
            'staff': forms.Select(attrs={'class': 'float-end'}),
        }
