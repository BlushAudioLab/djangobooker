from email.headerregistry import Group
from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    timebooked = models.DateTimeField(auto_now_add=True)
    # starttime = models.DateTimeField()
    # endtime = models.DateTimeField()
    
    def __str__(self):
        return self.title
    

class Room(models.Model):
    name = models.CharField(max_length=20)
    # update this one later
    type = models.CharField(max_length=20)
    capacity = models.CharField(max_length=2)
    description = models.CharField(max_length=500, null=True)
    # not sure about this bit
    def __str__(self):
        return self.name