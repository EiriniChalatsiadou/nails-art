from datetime import date
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Booking
from .forms import BookingForm
#To BE REMOVED
import logging, sys
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
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

def add_booking(request):
    if not request.user.is_authenticated:
        return render(request,'booking/list.html')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        logging.debug(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            return redirect('booking-list')
    else:
        # GET request, initialize the form
        form = BookingForm()

    context = {
        'form' : form
    }

    return render(request,'booking/add.html', context)





# class bookAtreatment(TemplateView):
#     """
#     Homepage
#     """

#     template_name = "book_a_treatment.html"