from django.forms import ModelForm
from .models import Post


class CustomPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'post']
