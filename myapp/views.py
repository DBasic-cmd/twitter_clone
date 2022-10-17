from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages


# Create your views here.
def home(request):
    posts = Post.objects.all().order_by("-id")
    form = PostForm(request.POST)
    entries = Post.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.info(request, 'you have successfully created a post.')
            return redirect('twitter-home')
    else:
        form = PostForm()
    context = {
        'posts':posts,
        'form': form,
        'entries': entries
    }
    return render(request, 'myapp/home.html',context)



def delete_view(request,id):
    post = get_object_or_404(Post,id=id)
    if request.user == post.user:
        post.delete()
        return redirect('twitter-home')
    else:
        return redirect('twitter-home')

def read(request, id):
    post = get_object_or_404(Post,id=id)
    context = {
        'post' :post,
    }
    return render(request, 'myapp/read.html', context)

def search(request):
    posts = Post.objects.all().order_by('-id')
    
    if request.method == 'GET':
        keyword=request.GET.get('keyword')
        if keyword:
            posts = posts.filter(content__icontains=keyword)
    form = PostForm()

    context = {
        'posts':posts,
        'form': form,
    }
    return render(request, 'myapp/home.html',context)