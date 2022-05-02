from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from categories.models import Article

class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish'),
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, allow_unicode=True, unique=True)
    author = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name='posts')
    body = RichTextField()
    publish = models.DateTimeField(default = timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1,
                            choices=STATUS_CHOICES,
                            default="p")
    category = models.ForeignKey(Article,
                            on_delete=models.CASCADE,
                            related_name='posts')

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post', args=[self.category.sub_category.category.slug,
                                    self.category.sub_category.slug,
                                    self.category.slug,
                                    self.slug])
