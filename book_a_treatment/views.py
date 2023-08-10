from datetime import date
from django.shortcuts import render
from django.db.models import Q
from .models import Booking
from .forms import BookingForm


# from django.views.generic import TemplateView

# Create your views here.
def get_booking_list(request):
    if not request.user.is_authenticated:
        return render(request,'booking/list.html')

    bookings = Booking.objects.filter(Q(user=request.user) & Q(date__gte=date.today()))
    context = {
        'bookings' : bookings
    }

    return render(request,'booking/list.html', context)



# class bookAtreatment(TemplateView):
#     """
#     Homepage
#     """

#     template_name = "book_a_treatment.html"