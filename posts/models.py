from django.db import models
from tinymce.models import HTMLField
import uuid
# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=500)
    post = HTMLField()
    is_ready_to_post = models.BooleanField(default=False)
    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)