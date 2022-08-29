from django.db import models
import uuid
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to = 'topics/')
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)
    #created and ID


    def __str__(self):
        return self.name
