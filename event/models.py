from django.db import models

from datetime import datetime


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Events(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    check = models.CharField(max_length=3, default='off')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(default=datetime.now())
