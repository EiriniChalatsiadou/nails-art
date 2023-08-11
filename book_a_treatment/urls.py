"""
Home App - URLS
----------------
URL Routing for Home App.
"""
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.bookAtreatment.as_view(), name='book-a-treatment'),
    path('', views.get_booking_list, name='booking-list'),
    path('add/', views.add_booking, name='add'),
]
