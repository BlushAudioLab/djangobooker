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
def about(request):
    return render (request,'about.html', {'title': 'About'})