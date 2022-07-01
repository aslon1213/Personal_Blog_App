from django.forms import ModelForm
from .models import Post


class CustomPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['owner', 'colloborators','title', 'post','preview','tags', 'is_ready_to_post', 'post_thumbnail']
