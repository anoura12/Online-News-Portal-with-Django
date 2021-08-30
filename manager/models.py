from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Manager(models.Model):
    name = models.CharField(max_length=50)
    utxt = models.TextField()  ## utxt for username
    email = models.TextField(default="")
    ip = models.TextField(default="") # Get User IP Address
    country = models.TextField(default="") # Get User Location
    is_premium = models.BooleanField(default=False)
        
    def __str__(self):
        return self.name