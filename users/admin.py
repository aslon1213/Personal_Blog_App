from django.contrib import admin
from .models import UserProfile, subscribers
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(subscribers)