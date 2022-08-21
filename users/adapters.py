from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth.models import User
from allauth.socialaccount.signals import pre_social_login
from .models import UserProfile
from django.dispatch import receiver


class MyLoginApp(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        email = sociallogin.account.extra_data['email']
        account = sociallogin.account
        data = account.extra_data
        if data['name']:
            username = data['name']
        else:
            username = email
        try:
            if User.objects.get(email = email):
                user = User.objects.get(email = email)
                #print(user.username)
                #print(user.email)
                return user
        except:
            # user_2 = UserProfile.objects.create(
            # user = sociallogin.user,
            # username = sociallogin.user.username,
            # email = sociallogin.user.email,
            # )
            # print(user_2)
            # user_2.save()
            return sociallogin.account
            
@receiver(pre_social_login)
def social_account_login(request, sociallogin, *args, **kwargs):
    email = sociallogin.account.extra_data['email']
    #user = sociallogin.user
    try:
        user = User.objects.get(email = email)
        sociallogin.connect(request,user)
    except:
        pass
    

