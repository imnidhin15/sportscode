from django.db import models


# Create your models here
class event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    team = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
