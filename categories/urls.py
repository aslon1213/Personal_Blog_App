from django.urls import path

from categories.views import Category, category


urlpatterns = [
    path('<str:category>',category, name = 'category')
]