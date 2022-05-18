from email.headerregistry import Group
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timebooked = models.DateTimeField(auto_now_add=True)
    room = models.ForeignKey(
        'Room', 
        null=True, 
        on_delete=models.CASCADE
    )
    starttime = models.DateTimeField(null=True, blank=True)
    endtime = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('event-detail', kwargs={'pk': self.pk})
    

class Room(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(
        'Type', 
        null=True, 
        on_delete=models.CASCADE
    )
    capacity = models.CharField(max_length=2)
    description = models.CharField(max_length=500, null=True, blank=True)
    # not sure about this bit
    def __str__(self):
        return self.name
    

class Type(models.Model):
    type = models.CharField(
        max_length=100,
        null=False,
        default='',
    )
    def __str__(self):
        return self.type
    
    
class Item(models.Model):
    class Type(models.TextChoices):
        microphone = '1', "Microphone"
        dibox = '2', "DI Box"
    
    name = models.CharField(max_length=40)
    barcode = models.IntegerField(default=800000)
    description = models.CharField(max_length=200)
    type = models.CharField(
        max_length=2,
        choices=Type.choices,
        default=Type.microphone
    )
    