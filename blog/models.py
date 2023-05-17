from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Article(models.Model):
    user_id = models.IntegerField()
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article_image', blank=True)
    tag = models.ManyToManyField(Tag, blank=True, related_name='articles')
    def __str__(self):
        return self.title
