from django.db import models
from django.urls import reverse

# Create your models here.
class ChallengeLevelChoices(models.TextChoices):
    EASY = 'Easy'
    MEDIUM = 'Medium'
    HARD = 'Hard'

class Challenge(models.Model):
    level = models.CharField(choices=ChallengeLevelChoices.choices, max_length=6)
    title = models.CharField(max_length=100)
    slug = models.SlugField(editable=False)
    category = models.ForeignKey('TaskCategory', default=1, on_delete=models.CASCADE)
    body = models.TextField()
    image = models.ImageField(upload_to='task_images', blank=True)
    duration = models.CharField(max_length=100, default='1 Day')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=100)
    optional = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('challenge', kwargs={'pk': self.pk})
    
    def save(self, *args, **kwargs):
        self.slug = self.title.replace(' ', '-').lower()
        super().save(*args, **kwargs)

class TaskCategory(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='task_category')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title 

class User_Task(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)   

    def __str__(self):
        return self.challenge.title