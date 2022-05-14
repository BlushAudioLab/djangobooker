from django.urls import path
from .views import EventListView
from . import views

urlpatterns = [
    path('home/', EventListView.as_view(), name='bookingsystem-home'),
    path('bookroom/', views.book, name='bookingsystem-bookroom'),
    path('reservation/', views.reserve, name='bookingsystem-reservation')
]