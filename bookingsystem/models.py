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
        'RoomType', 
        null=True, 
        on_delete=models.CASCADE
    )
    capacity = models.CharField(max_length=2)
    description = models.CharField(max_length=500, null=True, blank=True)
    # not sure about this bit
    def __str__(self):
        return self.name
    

class RoomType(models.Model):
    type = models.CharField(
        max_length=100,
        null=False,
        default='',
    )
    def __str__(self):
        return self.type
    

class Item(models.Model):
    name = models.CharField(max_length=20)
    barcode = models.CharField(max_length=6)
    description = models.CharField(max_length=500, null=True, blank=True)
    type = models.ForeignKey(
        'ItemType', 
        null=True, 
        on_delete=models.CASCADE
    )
    area = models.ForeignKey(
        'ItemArea',
        null=True,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.name
    

class ItemType(models.Model):
    type = models.CharField(
        max_length=100,
        null=False,
        default='',
    )
    def __str__(self):
        return self.type
    
    
class ItemArea(models.Model):
    area = models.CharField(
        max_length=20,
        null=False,
        default='',
    )
    def __str__(self):
        return self.area    
    
