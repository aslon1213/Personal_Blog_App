from django.urls import path
from .views import create_post, posts, post, edit_post
urlpatterns = [
    path('create_post/', create_post, name="create_post"),
    path('', posts, name='posts'),
    path('<str:pk>', post, name = 'post'),
    path('edit/<str:pk>/', edit_post, name = 'edit_post'),
]