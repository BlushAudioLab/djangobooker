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