from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='bookingsystem-home'),
    path('bookroom/', views.book, name='bookingsystem-bookroom'),
    path('reservation/', views.reserve, name='bookingsystem-reservation')
]