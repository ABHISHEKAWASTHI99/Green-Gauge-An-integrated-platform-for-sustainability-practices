from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class feedback(models.Model):
    user = models.CharField(max_length=100)
    feedback_type = models.CharField(max_length=100, choices=(('Bug', 'Bug'), ('Feature', 'Feature'), ('Other', 'Other')))
    feedback = models.TextField()

    def __str__(self):
        return self.feedback_type