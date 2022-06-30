from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserRegistrationForm, UserLoginForm
# Create your views here.
def register_user(request):
    form = UserRegistrationForm()
    context = {'form':form}
    return render(request, 'users/register.html', context)

def login_user(request):
    form = UserLoginForm()
    context = {'form':form}
    return render(request, 'users/login.html', context)
