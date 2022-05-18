from django.shortcuts import render
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
)


import bookingsystem
from .models import Event
from django.contrib.auth.decorators import login_required


def home(request):
    context = {
        'events': Event.objects.all()
    }
    return render (request,'home.html', context)


class EventListView(ListView):
    model = Event
    template_name = 'home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    ordering = ['-timebooked']


class EventDetailView(DetailView):
    model = Event
    
    
class EventCreateView(CreateView):
    model = Event
    fields = [
        'title',
        'room',
        'starttime',
        'endtime'
    ]
    

@login_required
def book(request):
    return render (request,'bookroom.html', {'title': 'Book a Room'})


@login_required
def reserve(request):
    return render (request,'reservation.html', {'title': 'Reserve Equipment'})