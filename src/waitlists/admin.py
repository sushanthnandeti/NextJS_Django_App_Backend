from django.contrib import admin

# Register your models here.

from .models import WaitListEntry

admin.site.register(WaitListEntry)