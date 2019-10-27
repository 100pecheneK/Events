from django.shortcuts import render
from django.http import HttpResponse


def view(request):
    # return render(request, 'users/users.html')
    if request.user.is_authenticated():
        return HttpResponse('YES')
    else:
        return HttpResponse('NO')


def register(request):
    return HttpResponse('register')


def login(request):
    return HttpResponse('login')


def logout(request):
    return HttpResponse('logout')
