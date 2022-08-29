
from cgitb import Hook
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from .models import Post, Comment
from django.utils.text import slugify
from .forms import CustomPostCreationForm

#redirects
from django.views.generic.base import RedirectView

HOST = 'https://127.0.0.0:8000'
SLUGIFIED_VERSION_OF_HOST = 'https%3A//127%2E0%2E0%2E0%3A8000'
#slugified_version_of_host = 'https%3A//something.com'
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
    links = make_post_urls(request)
    return render(request, 'posts/post.html', context={'post':post, 'comments':comments, 'share_on_links':links})


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


# class share_on_social_media(RedirectView)
#     def share_on_social_media(request,website_name):
        
        
        
        
#         path = "{HOST}{request.path}"
        

#         message = 'I found this article very interesting. Check it out {path}'

#     def get_redirect_url(*args, **kwargs):
#         websites = {
#             'twitter':"url",
#             'instagram':'url',
#             'copy_link':'url',
#         }
#         try:
#             link = websites[website_name]
#         except:
#             return messages.error('Error in request')
#         return link

#replace white spaces with %20 ( which is white space indication in urls)
def my_slugify(text):
    text_arr = text.split(" ")
    text = ''
    for t in text_arr:
        text += t + '%20'
    return text

# def slugify_url(url):
    
#     url = url.replace('/','%2F')


#     return url

def make_post_urls(request):
    path = SLUGIFIED_VERSION_OF_HOST + str(request.path)
    message = my_slugify('I found this article very interesting. Check it out')

    websites = {
        'twitter':'https://twitter.com/intent/tweet',
        'linkedin':'',
        'facebook':'',
        
        'instagram':'url',
    }
    links = {}
    for website in websites:
        links[website] = websites[website] + "/?url="+path+"&text="+message
        
    links['copy_link'] = HOST + request.path
    return links
#https://twitter.com/intent/tweet?url=https%3A//youtu.be/erjwCQ-UZyw&text=Forza%20Horizon%205%20Hot%20Wheels%20Expansion%20-%20First%2010%20minutes%20%7C%20Thrustmaster%20TX&via=YouTube&related=YouTube,YouTubeTrends,YTCreators
#                               url=https%3A127%2E0%2E0%2E0%3A8000%2Fposts%2F5fe9e4da-4085-4d68-a242-17f10a85afb3