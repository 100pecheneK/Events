from django.db import models

from datetime import datetime
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    check = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now())
