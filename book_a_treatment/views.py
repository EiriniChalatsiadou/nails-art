# Import necessary modules
from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Booking
from .forms import BookingForm

# Define view to get booking list
def get_booking_list(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return render(request,'booking/list.html')

    # Get bookings for the authenticated user with date greater than or equal to today
    bookings = Booking.objects.filter(Q(user=request.user) & Q(date__gte=date.today())).order_by('date')
    # Define context with bookings
    context = {
        'bookings' : bookings
    }

    # Render the booking list template with context
    return render(request,'booking/list.html', context)

# Define view to add a booking
def add_booking(request):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return render(request,'booking/list.html')

    # Handle POST request to add a booking
    if request.method == 'POST':
        form = BookingForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the booking with the current user
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            # Redirect to the booking list after successful addition
            return redirect('booking-list')
    else:
        # Handle GET request, initialize the form
        form = BookingForm()

    # Define context with the form
    context = {
        'form' : form
    }

    # Render the add booking template with context
    return render(request,'booking/add.html', context)


# Define view to edit a booking
def edit_booking(request, booking_id):
    # Check if the user is authenticated
    if not request.user.is_authenticated:
        return render(request,'booking/list.html')

    booking = get_object_or_404(Booking, id=booking_id)
    # Handle POST request to add a booking
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        # Check if the form is valid
        if form.is_valid():
            booking.save()
            # Redirect to the booking list after successful addition
            return redirect('booking-list')
    else:
        # Handle GET request, initialize the form
        form = BookingForm(instance=booking)

    # Define context with the form
    context = {
        'form' : form
    }

    # Render the add booking template with context
    return render(request,'booking/edit.html', context)

def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    booking.delete()
    return redirect('booking-list')