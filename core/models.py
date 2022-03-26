from django.db import models

# Create your models here.
class Post(models.Model):
    nomi = models.CharField(max_length=50)
    mazmuni = models.TextField()

    def __str__(self):
        return self.nomi