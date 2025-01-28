from django.shortcuts import render, get_object_or_404, redirect # type: ignore
from django.views.decorators.csrf import csrf_protect # type: ignore
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-created_at') #This is how we are arranging posts in Home page
    return render(request,'blog/home.html',{'posts':posts})

def post_detail(request,id):
    post = get_object_or_404(Post, id=id) # This is how we are getting the post
                                          # Basically we doing if else at the same line
    return render(request,'blog/post_detail.html',{'post':post})

def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Post.objects.create(title=title,content=content)
        return redirect('home')
    return render(request, 'blog/create_post.html')

# def delete_post(request, id):
#     post = get_object_or_404(Post, id=id)
#     post.delete()
#     return redirect('home')


def delete_post(request, id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=id)
        post.delete()
        return redirect('home')
    else:
        return HttpResponseNotAllowed(['POST']) # type: ignore



