from django.db import models

# Create your models here.


class Lines(models.Model):
    lineo = models.CharField(max_length=100)
    linet = models.CharField(max_length=100)
    lineth = models.CharField(max_length=100)
