from ast import Sub
from django.contrib import admin
from .models import UserProfile, Subscriber, Interest, StaffUsers
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Subscriber)
admin.site.register(Interest)
admin.site.register(StaffUsers)