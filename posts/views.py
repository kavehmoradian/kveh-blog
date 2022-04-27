from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .models import Post
from comments.forms import ReplyForm, CommentForm

class PostListView(ListView):
    queryset = Post.objects.all()
    context_object_name = "posts"
    template_name = "posts/posts.html"

def post(request, category, slug):
    comment_form = CommentForm()
    reply_form = ReplyForm()
    post = get_object_or_404(Post, slug=slug, category=category)
    template_name = "posts/post.html"
    return render(request, template_name, {'post': post,
                                'comment_form': comment_form,
                                'reply_form': reply_form})
