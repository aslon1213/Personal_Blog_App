from typing import List
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Topic
from posts.models import Post



class Category(ListView):
    model = Post
    context_object_name = "topic_list"
    template_name  = 'categories/category.html'
    def get_queryset(self): # new
        topic_name = self.category
        id_q = Topic.objects.get(name = topic_name)
        queryset = Post.objects.filter(topic = id_q.id)
        return queryset



def category(request, category):
    topic_name = category
    queryset = []
    try:
        id_q = Topic.objects.get(name = topic_name)
        queryset = Post.objects.filter(topic = id_q.id)
    except:
        return redirect('main')
    context = {
        "posts":queryset
    }
    return render(request, 'posts/posts.html', context)