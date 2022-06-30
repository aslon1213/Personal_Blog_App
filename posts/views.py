from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Post
from .forms import CustomPostForm
# Create your views here.
def create_post(request):
    form = CustomPostForm()
    
    if request.method == "POST":
        form = CustomPostForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form':form
    }
    return render(request, 'posts/create_post.html', context)

def posts(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'posts/posts.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'posts/post.html', context={'post':post})

def edit_post(request,pk):
    post = Post.objects.get(id=pk)
    form = CustomPostForm(instance=post)
    if request.method == "POST":
        form = CustomPostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'posts/edit_post.html', context)

