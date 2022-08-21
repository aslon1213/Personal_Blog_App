"""personal_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from posts.views import main_page, posts
urlpatterns = [
    path('admin/', admin.site.urls),
    #django - allauth
    path('accounts/', include('allauth.urls')),

    #different topics sections
    path('topics/', include('categories.urls')),

    #users app
    path('users/', include('users.urls')),
    #posts app
    path('posts/', include('posts.urls')),
    #tinymce
    path('tinymce/', include('tinymce.urls')),

    #start pages
    path('', posts, name = 'main'),
    path('', posts, name = 'home'),

    #django-debug tools when deploying this should be deleted
    path('__debug__/', include('debug_toolbar.urls')),
] 
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT, )
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = path('__debug__/', include(debug_toolbar.urls)) + urlpatterns

