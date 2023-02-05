from django.shortcuts import render
from .models import Post


# Create your views here.

def main_view(request):
    posts = Post.objects.all()
    return render(request, 'blogapp/index.html', context={'posts': posts})


def create_post(request):
    return render(request, 'blogapp/create.html')


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blogapp/post.html', context={'post': post})
