from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class StaffUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user_default.png")
    
    #socials
    twitter = models.CharField(max_length=200, blank=True, null=True)
    github = models.CharField(max_length=200, blank=True, null=True)
    linked_in = models.CharField(max_length=200, blank=True, null=True)
    youtube = models.CharField(max_length=200, blank=True, null=True)
    telegram = models.CharField(max_length=200, blank=True, null=True)
    website = models.CharField(max_length=200, blank=True, null=True)
    

    #interests
    interests = models.ManyToManyField('Interest',blank=True )

    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)
    

    #permissions
    
    def __str__(self) -> str:
        return str(self.username)

"""class newsletter_senders(models.Model):
    pass"""

class Subscriber(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=250)
    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return str(self.name)

#
#class Messages:
#

class Interest(models.Model):
    name = models.CharField(max_length=200, null=True)
    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name