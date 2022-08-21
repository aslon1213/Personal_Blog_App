
from cProfile import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from django.contrib import messages
#models
from .models import UserProfile, Subscriber
from django.contrib.auth.models import User
#forms
from .forms import UserLoginForm, UserRegistrationForm, SubscriberForm, EditAccountForm
#utils
from .utils import check_password_req


def register_user(request):
    if request.user.is_authenticated:
        messages.success(request,'You should first logout')
        return redirect('posts')
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #getting form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            if check_password_req(password_1, password_2) == 1:
                #creating User object
                user = User.objects.create(
                    username = username,
                    email = email,
                    password = password_1
                )
                #creating UserProfile object and connecting it UserProfile
                userprofile = UserProfile.objects.create(
                    user = user,
                    username = user.username,
                    email = user.email,
                )
                messages.success(request,'User was succesfully registered')
                return redirect('login')
            else:
                messages.error(request,check_password_req(password_1, password_2))
        else:
            messages.success(
                request, 'An error has occurred during registration')
    context = {'form':form}
    return render(request, 'users/register.html', context)


def login_user(request):
    form = UserLoginForm()
    if request.user.is_authenticated:
        return redirect('posts')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = UserProfile.objects.get(username=username) 
            #later should be changed - after signals have been implemented 
            username = user.user.username
        except:
            messages.error(request, "Wrong username ")

        user = authenticate(request, username=username, password=password)        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back {username} ")
            return redirect('posts')
        else:
            messages.error(request, 'Wrong password')
            return redirect('login')

    context = {"form":form}
    return render(request, 'users/login.html', context)


def logout_user(request):
    logout(request)
    messages.success(request,'User was logget out')
    return redirect('account_login')


def register_subscriber(request):
    if request.method == "POST":
        email = request.POST['email']
        name = request.POST['name']
        Subscriber.objects.create(
            name = name,
            email = email
        )
        messages.success(request, 'Thank you for subscribing')
        return redirect('posts')


@login_required(login_url='login')
def account_page(request):
    profile = request.user.userprofile
    context = {'profile':profile}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def edit_profile(request):
    profile = request.user.userprofile
    form = EditAccountForm()

    context = {'form':form}
    return render(request, 'users/account_edit_form.html', context)


def contributors_page(request):
    profiles = Profile.objects.all()


def add_interests(interest_list):
    pass


            