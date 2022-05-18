from django.urls import path
from .views import (EventListView, 
                    EventDetailView, 
                    EventCreateView,
)
from . import views

urlpatterns = [
    path('home/', EventListView.as_view(), name='bookingsystem-home'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    path('event/new/', EventCreateView.as_view(), name='event-create'),
    path('bookroom/', views.book, name='bookingsystem-bookroom'),
    path('reservation/', views.reserve, name='bookingsystem-reservation')
]