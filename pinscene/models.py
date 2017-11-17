from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=200)
    notes = models.TextField(default='blank')

    def __str__(self):
        return self.name

class Pin(models.Model):
    """A Pin represents an individual pinball machine"""
    title = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=360)
    year = models.IntegerField()
    designer = models.CharField(max_length=200)
    played = models.BooleanField(default=False)
    note = models.TextField()

    def __str__(self):
        """Return string representation of the model"""
        return self.title

