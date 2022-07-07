from ast import For
from django.forms import ModelForm, Form
from .models import Post

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout




class CustomPostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['colloborators','title', 'post','preview','tags', 'is_ready_to_post', 'post_thumbnail']
