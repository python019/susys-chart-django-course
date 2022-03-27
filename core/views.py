from django.shortcuts import render
from .models import Post

def home(request):
    return render(request, 'index.html')

def example(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'examp.html', context)