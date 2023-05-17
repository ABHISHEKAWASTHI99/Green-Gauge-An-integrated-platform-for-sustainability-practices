from django.db import models
# Create your models here.

class Userprofile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
