from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='bookingsystem-login'),
    path('logout/', views.logout, name='bookingsystem-logout'),
]