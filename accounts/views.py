from django.views.generic import FormView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


class Signup(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = 'accounts/signup.html'

    def form_valid(self, form):
        form.save()
        return super(Signup, self).form_valid(form)


class Login(FormView):
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(Login, self).form_valid(form)


class Logout(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
