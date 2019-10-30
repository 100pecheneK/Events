from django.db import models
from event.models import Category


# Create your models here.
class Account(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=400)

    def save(self, **kwargs):
        super(Account, self).save(**kwargs)
        Category.objects.create(user=Account, title='Без категории')

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'
