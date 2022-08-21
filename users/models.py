from django.db import models
from django.contrib.auth.models import User
import uuid

#   for login activites
#from django.db.models.signals import post_save, post_delete
#from allauth.socialaccount.signals import (pre_social_login)
#from django.dispatch import receiver
#from django.db.models.signals import (pre_save, post_save, pre_delete, post_delete)
#from django.contrib.auth import login, authenticate
#from django.contrib import messages
#from allauth.account.adapter import DefaultAccountAdapter
class StaffUsers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    age = models.IntegerField(null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user_default.png")

    #info
    short_info = models.CharField(max_length=500, null=True, blank=True)
    extended_info = models.TextField(null=True, blank=True)

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
        if self.username:
            return str(self.username)
        else:
            return str(self.email)


# class newsletter_senders(models.Model):
#     pass

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




# @receiver(pre_social_login)
# def print_social_account(request, sociallogin, *args, **kwargs):
#     if (sociallogin.account.provider.lower() == 'google'):
#         provider = sociallogin.account.provider
#         email = sociallogin.account.extra_data['email']
#         name = sociallogin.account.extra_data['name']
#         first_name = sociallogin.account.extra_data['given_name']
#         last_name = sociallogin.account.extra_data['family_name']
#         try:
#             if User.objects.get(email = email):
#                 social_user = User.objects.get(email = email)
#                 messages.success(request, 'You are logged in.')
#                 login(request, social_user, backend = 'django.contrib.auth.backends.ModelBackend')
#                 messages.success(request, 'You are logged in woogoo.')
#         except User.DoesNotExist:
#             user = User.objects.create_user(email, email, 'password')
#             user.first_name = first_name
#             user.last_name = last_name
#             user.save()
#             user_profile = UserProfile.objects.create(user = user, name = name, email = email)
#             user_profile.save()
#             messages.success(request, 'User created')
#             login(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
