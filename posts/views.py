from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "posts/posts.html"

def post(request, category, slug):
    post = get_object_or_404(Post, slug=slug, category=category)
    template_name = "posts/post.html"
    return render(request, template_name, {'post': post})
