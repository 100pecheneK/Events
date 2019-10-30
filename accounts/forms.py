from django import forms


class AccountForm(forms.Form):
    login = forms.CharField(label='Your name', required=True)
    password = forms.CharField(label='Password', required=True)

