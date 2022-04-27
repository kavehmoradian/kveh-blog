from django.db import models
from posts.models import Post

class Comment(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return self.name + " ---> " + self.date

class Reply(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replys')

    class Meta:
        ordering = ('date', )

    def __str__(self):
        return self.name + " ---> " + self.date
