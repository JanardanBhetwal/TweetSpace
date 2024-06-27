from django.contrib import admin
from .models import Tweet

# Register your models here.
admin.site.register(Tweet)  # This will make the Tweet model visible on the admin page