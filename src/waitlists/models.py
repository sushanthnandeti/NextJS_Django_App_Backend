from django.db import models

# Create your models here.

class WaitListEntry(models.Model): 
    # user = 

    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

