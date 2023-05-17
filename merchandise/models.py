from django.db import models

# Create your models here.
class Merchandise(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    description = models.TextField(default='')
    image = models.ImageField(upload_to='merchandise', blank=True)

    def __str__(self):
        return self.name
        