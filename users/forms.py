from cProfile import Profile
from django.forms import ModelForm
from .models import UserProfile
from django.contrib.auth.models import User

class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']