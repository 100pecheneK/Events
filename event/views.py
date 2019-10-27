from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Events, Category
from accounts.models import Account

from datetime import datetime


# Create your views here.
def view(request, cat_id=0):
    context = dict()
    if (cat_id):
        events = Events.objects.filter(category_id=int(cat_id)).order_by('-date')
        categorySingle = Category.objects.get(id=cat_id)
        context = {
            'categorySingle': categorySingle,
        }
    else:
        events = Events.objects.all().order_by('-date')
    category = Category.objects.all()



    context['events'] = events
    context['category'] = category

    return render(request, 'events/events.html', context)


# def viewCategory(request):


def create(request):
    category = int(request.POST['category'])
    cat = Category.objects.get(id=category)

    try:
        check = request.POST['check']
        check = 1
    except:
        check = 0

    cat.events_set.create(
        title=request.POST['title'],
        text=request.POST['text'],
        check=check
    )
    # category_id = request.POST['category']
    # category = Category.objects.get(id=int(category_id))
    #
    # category.events_set.

    return HttpResponseRedirect(reverse('event:events'))
    # return HttpResponse(request.POST['category'])


def edit(request, even_id):
    event = Events.objects.get(id=even_id)
    event.title = request.POST['title']
    event.text = request.POST['text']
    event.category_id = int(request.POST['category'])
    try:
        check = request.POST['check']
        event.heck = 1
    except:
        event.check = 0
    event.date = datetime.now()
    event.save()
    # category = Category.objects.get(events_id=even_id)

    return HttpResponseRedirect(reverse('event:events'))


def delete(request, even_id):
    event = Events.objects.get(id=even_id)
    event.delete()

    return HttpResponseRedirect(reverse('event:events'))


def category_create(request):
    Category.objects.create(
        title=request.POST['title']
    )
    return HttpResponseRedirect(reverse('event:events'))


def category_edit(request, cat_id):
    category = Category.objects.get(id=cat_id)
    category.title = request.POST['title']
    category.save()
    return HttpResponseRedirect(reverse('event:events'))


def category_delete(request, cat_id):
    category = Category.objects.get(id=cat_id)
    category.delete()
    return HttpResponseRedirect(reverse('event:events'))
