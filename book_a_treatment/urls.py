"""
Home App - URLS
----------------
URL Routing for Home App.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_booking_list, name='booking-list'),
    path('add/', views.add_booking, name='add-booking'),
    path('edit/<booking_id>', views.edit_booking, name='edit-booking'),
    path('delete/<booking_id>', views.delete_booking, name='delete-booking'),
]
