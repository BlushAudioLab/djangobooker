from django.urls import path
from .views import EventListView, EventDetailView
from . import views

urlpatterns = [
    path('home/', EventListView.as_view(), name='bookingsystem-home'),
    
    path('event/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    
    
    path('bookroom/', views.book, name='bookingsystem-bookroom'),
    path('reservation/', views.reserve, name='bookingsystem-reservation')
]