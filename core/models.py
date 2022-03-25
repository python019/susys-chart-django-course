from django.db import models

# Create your models here.
class Post(models.Model):
    nomi = models.CharField(max_length=50)