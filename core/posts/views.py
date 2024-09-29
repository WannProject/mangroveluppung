from django.shortcuts import render
from .models import Post
# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html',{'posts': posts})

def post_page(request, slug):
    post = Post.objects.get(slug=slug)  # Mendapatkan post berdasarkan slug
    return render(request, 'posts/posts_detail.html', {'post': post})