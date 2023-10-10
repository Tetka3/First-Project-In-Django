from django.db import models

# Create your models here.
class Trip(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    nights = models.IntegerField()
    price = models.IntegerField()