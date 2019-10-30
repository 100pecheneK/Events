from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

from .models import Events, Category


def view(request, categoryId=0):
    context = dict()
    if request.user.is_authenticated:
        if (categoryId):
            events = Events.objects.filter(category_id=int(categoryId), user=request.user).order_by('-date')
            category = Category.objects.get(id=categoryId, user=request.user)
            context = {
                'category': category,
            }
        else:
            events = Events.objects.filter(user=request.user).order_by('-date')

        categories = Category.objects.filter(user=request.user)

        context['events'] = events
        context['categories'] = categories
        return render(request, 'events/events.html', context)
    else:
        return HttpResponseRedirect(reverse('accounts:signup'))


def create(request):
    if request.user.is_authenticated:
        chosenCategory = int(request.POST['category'])
        categoryObject = Category.objects.get(id=chosenCategory)
        try:
            check = request.POST['check']
        except:
            check = 'off'

        categoryObject.events_set.create(
            user=request.user,
            title=request.POST['title'],
            text=request.POST['text'],
            check=check
        )

        return HttpResponseRedirect(reverse('event:events'))
    else:
        return HttpResponseRedirect(reverse('accounts:signup'))


def edit(request, eventId):
    if request.user.is_authenticated:
        event = Events.objects.get(id=eventId)
        event.title = request.POST['title']
        event.text = request.POST['text']
        event.category_id = int(request.POST['category'])
        try:
            event.check = request.POST['check']
        except:
            event.check = 'off'
        event.date = datetime.now()
        event.save()

        return HttpResponseRedirect(reverse('event:events'))
    else:
        return HttpResponseRedirect(reverse('accounts:signup'))


def delete(request, eventId):
    if request.user.is_authenticated:
        event = Events.objects.get(id=eventId)
        event.delete()

        return HttpResponseRedirect(reverse('event:events'))
    else:
        return HttpResponseRedirect(reverse('accounts:signup'))


def category_create(request):
    if request.user.is_authenticated:
        Category.objects.create(
            user=request.user,
            title=request.POST['title']
        )

        return HttpResponseRedirect(reverse('event:events'))
    else:
        return HttpResponseRedirect(reverse('accounts:signup'))


def category_edit(request, categoryId):
    if request.user.is_authenticated:
        category = Category.objects.get(id=categoryId)
        category.title = request.POST['title']
        category.save()

        return HttpResponseRedirect(reverse('event:events'))
    else:
        return HttpResponseRedirect(reverse('accounts:signup'))


def category_delete(request, categoryId):
    if request.user.is_authenticated:
        category = Category.objects.get(id=categoryId)
        category.delete()

        return HttpResponseRedirect(reverse('event:events'))
    else:
        return HttpResponseRedirect(reverse('accounts:signup'))
