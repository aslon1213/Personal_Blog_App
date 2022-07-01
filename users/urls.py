from .views import (login_user, register_user,
    account,
    logout_user,
    register_subscriber
)
from django.urls import path


urlpatterns = [

    #
    path('register/', register_user, name = 'register' ),
    path('login/', login_user, name = 'login' ),
    path('logout/', logout_user, name = 'logout'),
    path('account/', account, name = 'account'),
    path('register_subscriber/', register_subscriber, name = 'subscribe'),

]