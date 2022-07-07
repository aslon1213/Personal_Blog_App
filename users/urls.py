from .views import (login_user, register_user,
    logout_user,
    register_subscriber,
    account_page,
)
from django.urls import path


urlpatterns = [

    #
    path('register/', register_user, name = 'register' ),
    path('login/', login_user, name = 'login' ),
    path('logout/', logout_user, name = 'logout'),
    path('register_subscriber/', register_subscriber, name = 'subscribe'),

    path('account/', account_page, name = 'account'),

]