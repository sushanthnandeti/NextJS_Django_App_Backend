from django.db import models

# Create your models here.

class WaitListEntry(models.Model): 
    # user = 

    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

