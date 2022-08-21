from allauth.socialaccount.signals import (pre_social_login)
from django.dispatch import receiver
from django.contrib.signals import (pre_save, post_save, pre_delete, post_delete)
@receiver(pre_social_login)
def print_social_account(request, sociallogin, *args, **kwargs):
    print(*args, **kwargs)
    print(sociallogin.account.extra_data)


@receiver(pre_social_login)
def print_social_connection(request, sociallogin, *args, **kwargs):
    print(*args, **kwargs)
    print(sociallogin.account.extra_data)
    print(sociallogin.account.extra_data['email'])
    print(sociallogin.account.extra_data['first_name'])
    print(sociallogin.account.extra_data['last_name'])
    print(sociallogin.account.extra_data['profile_image_url'])
    print(sociallogin.account.extra_data['profile_image_url_https'])
    print(sociallogin.account.extra_data['id'])
    print(sociallogin.account.extra_data['url'])
    print(sociallogin.account.extra_data['username'])
    print(sociallogin.account.extra_data['verified'])
    print(sociallogin.account.extra_data['email'])
    print(sociallogin.account.extra_data['email_verified'])
    print(sociallogin.account.extra_data['location'])
    print(sociallogin.account.extra_data['description'])
    print(sociallogin.account)

@receiver(pre_save)
def pre_save_print(sender, instance, *args, **kwargs):
    print("pre_save_print")
    print(sender)
    print(instance)
    print(args)
    print(kwargs)
@receiver(post_save)
def post_save_print(sender, instance, *args, **kwargs):
    print("post_save_print")
    print(sender)
    print(instance)
    print(args)
    print(kwargs)