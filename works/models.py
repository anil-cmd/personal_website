from django.db import models

# Create your models here.


class Projects(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    description = models.TextField(max_length=200)
    url = models.URLField(max_length=100)

    def __str__(self):
        return self.name
