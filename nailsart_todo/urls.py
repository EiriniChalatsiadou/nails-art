"""nailsart_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import login, signup, logout

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        '',
        include('home.urls'),
        name='home-urls'),
    path(
        'about-us',
        include('about_us.urls'),
        name='about.us-urls'),
    path(
        'contact',
        include('contact.urls'),
        name='contact-urls'),
    path(
        'treatments',
        include('treatments.urls'),
        name='treatments-urls'),
    path(
        'book-a-treatment/',
        include('book_a_treatment.urls'),
        name='book-a-treatment-urls'),
    path(
        'accounts/',
        include('allauth.urls')),
]
