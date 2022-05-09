from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

events = [
    {
        'title': 'Mixing Session 2',
        'owner': 'Baloo',
        'timebooked': '2nd April, 1987',
    },
    {
        'title': 'Big Drum Time',
        'owner': 'Greg the Man',
        'timebooked': '5th May, 2022',
    },
    {
        'title': 'Eggy Rhythms',
        'owner': 'David Featherstone',
        'timebooked': '9th May, 2022',
    },
    {
        'title': 'A Small Guitar',
        'owner': 'Emily Grifflin',
        'timebooked': '9th May, 2022',
    }
]


def home(request):
    context = {
        'events': events
    }
    return render (request,'home.html', context)


def about(request):
    return render (request,'about.html', {'title': 'About'})