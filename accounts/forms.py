from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from accounts.tools import tools


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
            tools.change_widget_attrs_class_to_invalid(self, 'username', 'Имя пользователя')
            user = User.objects.get(username=username)
            raise ValidationError('Имя пользователя занято')
        except User.DoesNotExist:
            tools.change_widget_attrs_class_to_valid(self, 'username', 'Имя пользователя')
            return username

    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.data['password2']
        if password != password2:
            tools.change_widget_attrs_class_to_invalid(self, 'password', 'Пароль')
            tools.change_widget_attrs_class_to_invalid(self, 'password2', 'Пароль ещё раз')
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
            tools.change_widget_attrs_class_to_valid(self, 'username', 'Имя пользователя')
        except User.DoesNotExist:
            tools.change_widget_attrs_class_to_invalid(self, 'username', 'Имя пользователя')
            raise ValidationError('Пользователя не существует')
        return username

    def clean_password(self):
        username = self.data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            tools.change_widget_attrs_class_to_invalid(self, 'password', 'Пароль')
            raise ValidationError('Пароль не верный')
        return password
