# from django.forms import forms
from django import forms
from .models import Account


class AccountForm(forms.Form):
    # fields = {
    #     'login',
    #     'password'
    # }
    login = forms.CharField(label='Your name', required=True)
    password = forms.CharField(label='Password', required=True)

