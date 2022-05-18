from django.shortcuts import render
from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin
    )
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


class EventListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'events'
    ordering = ['-timebooked']


class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    
    
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    fields = [
        'title',
        'room',
        'starttime',
        'endtime'
    ]
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    fields = [
        'title',
        'room',
        'starttime',
        'endtime'
    ]
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        event = self.get_object()
        if self.request.user == event.owner:
            return True
        return False
    
    
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    success_url = '/home/'

    def test_func(self):
        event = self.get_object()
        if self.request.user == event.owner:
            return True
        return False
        
    
    
@login_required
def book(request):
    return render (request,'bookroom.html', {'title': 'Book a Room'})


@login_required
def reserve(request):
    return render (request,'reservation.html', {'title': 'Reserve Equipment'})