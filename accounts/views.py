from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import FormView
from .forms import RegisterForm, LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class RegisterView(FormView):
    form_class = RegisterForm
    page_title = 'Register'
    template_name = 'accounts/register.html'

    def get(self, request):
        form = RegisterForm()
        return super(RegisterView, self).get(request, form=form)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            new_profile = User.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            if new_profile:
                return HttpResponseRedirect(reverse('accounts:login'))

        return super(RegisterView, self).get(request, form=form)


class LoginView(FormView):
    form_class = LoginForm
    page_title = 'Login'
    template_name = 'accounts/login.html'

    def get(self, request):
        form = LoginForm()
        return super(LoginView, self).get(request, form=form)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('event:events'))

        return super(LoginView, self).get(request, form=form)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))
