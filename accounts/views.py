from django.views.generic import FormView
from django.contrib.auth import login
# from django.views.generic.edit import FormView

from .forms import AccountForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


class Signup(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/accounts/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(Signup, self).form_valid(form)


class Login(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = 'accounts/login.html'

    # В случае успеха перенаправим на главную.
    success_url = '/'

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(Login, self).form_valid(form)


class Logout(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")
