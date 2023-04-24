from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views

from . import views as users_views
from django.urls import path



urlpatterns = [
    path('', users_views.home, name='home'),
    path('about-us/', users_views.about, name='about'),
    path('contact-us/', users_views.contact, name='contact'),
    path('Our-services/', users_views.services, name='services'),

    # Services routes   
    path('services/procurement', users_views.procurement, name='procurement'),
    path('services/chemicals', users_views.chemicals, name='chemicals'),
    path('services/equipment-rental', users_views.equipment, name='equipment'),
    path('services/marine-logistic', users_views.marine, name='marine'),
    path('services/civil-works', users_views.civil, name='civil'),
    path('services/skilled-manpower', users_views.manpower, name='manpower'),


]


