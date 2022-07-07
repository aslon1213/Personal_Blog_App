from django.db import models
from tinymce.models import HTMLField
import uuid
from users.models import UserProfile
# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)
    colloborators = models.ManyToManyField(UserProfile, related_name='colloborators', blank=True, null=True)
    title = models.CharField(max_length=500, null=True)
    preview = models.CharField(max_length=100, null=True, blank=True)
    post = HTMLField()
    post_thumbnail = models.ImageField(null = True, blank = True, upload_to='posts/')
    tags = models.ManyToManyField('Tag', blank=True)
    #number
    is_ready_to_post = models.BooleanField(default=False)
    views_count = models.IntegerField(default=0)
    comments_count = models.IntegerField(default=0)
    votes_total = models.IntegerField(default=0)
    votes_ratio = models.IntegerField(default=0)
    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)

    def get_colloborators_id(self):
        colloborators_id_list = self.colloborators.all().values_list('id')
        return colloborators_id_list

    def update_views_count(self, num):
        self.views_count += num
        self.save()
    
    def update_views_count_by_1(self):
        self.views_count += 1


    @property
    def update_comments_count(self):
        self.comments_count =  self.comments.all().count()

    @property
    def update_vote_ratio(self):
        self.votes_total = self.vote_set.count()
        upvotes = self.vote_set.filter(value = 'up').count()
        if self.votes_total > 0:
            self.votes_ratio = int(upvotes / self.votes_total) / 100

        self.save()

    class Meta:
        ordering = ['-created']
    

    def __str__(self) -> str:
        return str(self.title)

class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)
    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.user.username

class Vote(models.Model):
    """"""
    VOTE_TYPE = (
        ('Up','Up Vote'),
        ('Down', 'Down Vote')
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, null=True, on_delete=models.CASCADE)
    value = models.CharField (choices=VOTE_TYPE, max_length=100)
    #id and created time
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)


    def __str__(self) -> str:
        return str(self.value)


class Tag(models.Model):
    name = models.CharField(blank=True, null=True, max_length=60)
    #id and created time
    id = models.UUIDField(default = uuid.uuid4,unique=True, primary_key=True, editable=False)


    def __str__(self) -> str:
        return str(self.name)