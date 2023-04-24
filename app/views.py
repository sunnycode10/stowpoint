import re
from urllib import response
from django.shortcuts import render, redirect
from django.http import HttpResponse





def home(request):
    context= {}
    return render(request, 'index-3.html', context)


def about(request):
    context= {}
    return render(request, 'about.html', context)


def contact(request):
    context= {}
    return render(request, 'contact.html', context)


def services(request):
    context= {}
    return render(request, 'service-3.html', context)


# List of services 


def procurement(request):
    context= {}
    return render(request, 'procurement.html', context)


def chemicals(request):
    context= {}
    return render(request, 'chemicals.html', context)


def equipment(request):
    context= {}
    return render(request, 'equipment.html', context)

def marine(request):
    context= {}
    return render(request, 'marine.html', context)

def civil(request):
    context= {}
    return render(request, 'civil.html', context)

def manpower(request):
    context= {}
    return render(request, 'skilled.html', context)
