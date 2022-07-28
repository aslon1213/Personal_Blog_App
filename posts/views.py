
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Post, Comment
from .forms import CustomPostCreationForm
# Create your views here.
@login_required(login_url = 'login')
def create_post(request):
    form = CustomPostCreationForm()
    
    if request.method == "POST":
        profile = request.user.userprofile
        form = CustomPostCreationForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = profile
            post.save()
            return redirect('posts')
            
    context = {
        'form':form
    }
    return render(request, 'posts/create_post.html', context)

def posts(request):
    numbers = {
        1:'One',
        2:'Two',
        3:'Three',
        4:'Four',
        5:'Five'
    }
    posts = Post.objects.all()
    latest_posts = posts[:3]
    context = {'posts':posts, 'latest_posts':latest_posts, 'numbers':numbers}
    
    return render(request, 'posts/posts.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    if request.user.is_authenticated:
        authentificated_profile = request.user.userprofile

    if request.method == "POST":
        comment_body = request.POST['comment_body']
        comemnt = Comment.objects.create(
            content = comment_body,
            user = authentificated_profile,
            post = post,
        )
        messages.success(request, 'You made a comment')
    comments = post.comments.all()
    post.update_views_count(1)
    
    return render(request, 'posts/post.html', context={'post':post, 'comments':comments})

@login_required(login_url = 'login')
def edit_post(request,pk):
    profile = request.user.userprofile
    post = Post.objects.get(id=pk)
    if profile.id != post.owner.id and profile not in post.get_colloborators_id():
        messages.error(request, 'You are not owner or colloborator of this Post')
        return redirect('post', pk)
    
    form = CustomPostCreationForm(instance=post)
    if request.method == "POST":
        form = CustomPostCreationForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    context = {
        'form':form,
        'post':post,
    }
    return render(request, 'posts/edit_post.html', context)

@login_required(login_url = 'login')
def delete_post(request, pk):
    profile = request.user.userprofile
    post = Post.objects.get(id=pk)
    if profile.id != post.owner.id:
        messages.error(request, "You are not owner of this post")
        messages.info(request, 'Only owner can edit this post')
        return redirect('post', pk)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, 'Post has been deleted succesfully')
        return redirect('post', pk)

    
    context = {'id': post.id}
    return render(request, 'posts/delete_confirmation.html', context)


def main_page(request):
    context = {}
    return render(request, 'main.html', context)

# def create_comment()
# def vote()
#messaging 