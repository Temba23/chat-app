from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Message(models.Model):
    message = models.CharField(max_length=500)
    time = models.DateTimeField(default = datetime.now())
    user = models.CharField(max_length=100)
    room = models.CharField(max_length=100)

    def __str__(self) :
        return self.message
