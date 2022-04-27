from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from .models import Reply, Comment
from posts.models import Post
from .forms import ReplyForm, CommentForm

def add_comment(request, post_id):
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            post = get_object_or_404(Post, id=post_id)
            new_comment.post = post
            new_comment.save()
            messages.add_message(request, messages.SUCCESS, 'comment added.')
        else:
            messages.add_message(request, messages.ERROR, 'something went wrong.')
    return redirect(post.get_absolute_url())

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    post = comment.post
    comment.delete()
    messages.add_message(request, messages.SUCCESS, 'comment deleted.')
    return redirect(post.get_absolute_url())

def add_reply(request, comment_id):
    if request.method == 'POST':
        reply_form = ReplyForm(data=request.POST)
        if reply_form.is_valid():
            new_reply = reply_form.save(commit=False)
            comment = get_object_or_404(Comment, id=comment_id)
            new_reply.comment = comment
            new_reply.save()
            messages.add_message(request, messages.SUCCESS, 'reply added.')
        else:
            messages.add_message(request, messages.ERROR, 'something went wrong.')
    return redirect(comment.post.get_absolute_url())

def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    post = reply.comment.post
    reply.delete()
    messages.add_message(request, messages.SUCCESS, 'reply deleted.')
    return redirect(post.get_absolute_url())
