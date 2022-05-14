from django.shortcuts import render
from .models import Event
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render (request,'home.html', context)


@login_required
def book(request):
    return render (request,'bookroom.html', {'title': 'Book a Room'})


@login_required
def reserve(request):
    return render (request,'reservation.html', {'title': 'Reserve Equipment'})