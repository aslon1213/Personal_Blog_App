from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import UserProfile, subscribers
from .forms import UserRegistrationForm, SubscriberForm
# Create your views here.
def register_user(request):
    if request.user.is_authenticated:
        messages.success('You should first logout')
        return redirect('posts')
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userform = form.save(commit=False)
            userform = userform.username.lower()
            userform.save()
            messages.success(request,'User was succesfully registered')
            return redirect('login')
        else:
            messages.success(
                request, 'An error has occurred during registration')
    context = {'form':form}
    return render(request, 'users/register.html', context)

def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('posts')
    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = UserProfile.objects.get(username=username) 
            #later should be changed - after signals have been implemented 
            username = user.user.username
        except:
            messages.error(request, "Wrong username ")

        user = authenticate(request, username=username, password=password)        
        print(user)
        if user is not None:
            login(request, user)
            return redirect('posts')
        else:
            messages.error(request, 'Wrong password')
            return redirect('login')
    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.success(request,'User was logget out')
    return redirect('login')


def account(request):
    context = {}
    render(request, 'users/account.html', context)


def register_subscriber(request):
    form = SubscriberForm()
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {'form':form}
    return render(request, 'users/subscribe.html', context)
            


#login