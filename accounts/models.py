from django.db import models

# Create your models here.
class Account(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=400)
