from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='bookingsystem-home'),
    path('about/', views.about, name='bookingsystem-about'),
]