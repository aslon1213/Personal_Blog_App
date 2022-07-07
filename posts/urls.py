from django.urls import path
from .views import create_post, delete_post, posts, post, edit_post
urlpatterns = [
    path('create_post/', create_post, name="create_post"),
    path('', posts, name='posts'),
    path('<str:pk>', post, name = 'post'),
    path('<str:pk>/edit/', edit_post, name = 'edit_post'),
    path('<str:pk>/delete/', delete_post, name='delete_post'),
]