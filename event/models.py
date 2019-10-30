from django.db import models
from django.conf import settings


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Events(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    check = models.CharField(max_length=3, default='off')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now=True)
