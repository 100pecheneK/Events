from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate


class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя пользователя',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль ещё раз',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    class Meta:
        model = User
        fields = {'username', 'password'}

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            self.fields['username'].widget.attrs.update({
                'placeholder': 'Имя пользователя',
                'class': 'form-control is-invalid',
                'autocomplete': 'off'
            })
            user = User.objects.get(username=username).exists()
            raise ValidationError('Имя пользователя занято')
        except:
            return username

    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.data['password2']
        if password != password2:
            self.fields['password'].widget.attrs.update({
                'placeholder': 'Пароль',
                'class': 'form-control is-invalid',
                'autocomplete': 'off'
            })
            self.fields['password2'].widget.attrs.update({
                'placeholder': 'Пароль ещё раз',
                'class': 'form-control is-invalid',
                'autocomplete': 'off'
            })
            raise ValidationError('Пароли не совпадают')
        return password


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Имя пользователя',
        'class': 'form-control',
        'autocomplete': 'off'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    fields = {'username', 'password'}

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            user = User.objects.get(username=username)
        except:
            self.fields['username'].widget.attrs.update({
                'placeholder': 'Имя пользователя',
                'class': 'form-control is-invalid',
                'autocomplete': 'off'
            })
            raise ValidationError('Пользователя не существует')
        return username

    def clean_password(self):
        username = self.data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            self.fields['password'].widget.attrs.update({
                'placeholder': 'Пароль',
                'class': 'form-control is-invalid',
                'autocomplete': 'off'
            })
            raise ValidationError('Пароль не верный')
        return password
