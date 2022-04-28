from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    class Meta:
        ordering = ('order', )

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category,
                            on_delete=models.CASCADE,
                            related_name='subcategory')
    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sub_category = models.ForeignKey(SubCategory,
                            on_delete=models.CASCADE,
                            related_name='article')
    decsription = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/Article')
    def __str__(self):
        return self.name
