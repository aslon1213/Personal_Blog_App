from django.db import models
from django.contrib.auth.models import User
import uuid


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user_default.png")
    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)
    

    def __str__(self) -> str:
        return str(self.username)

"""class newsletter_senders(models.Model):
    pass"""