from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from event.models import Events, Category
from event.tools import tools


@login_required()
def view(request, categoryId=0):
    context = dict()
    if (categoryId):
        events = Events.objects.filter(category_id=categoryId, user=request.user).order_by('-date')
        category = Category.objects.get(id=categoryId, user=request.user)
        context['category'] = category
    else:
        events = Events.objects.filter(user=request.user).order_by('-date')

    categories = Category.objects.filter(user=request.user)

    context['events'] = events
    context['categories'] = categories
    return render(request, 'events/events.html', context)


@login_required()
def create(request):
    check = tools.get_check(request)
    category = tools.get_category(request, Category)
    category.events_set.create(
        user=request.user,
        title=request.POST['title'],
        text=request.POST['text'],
        check=check
    )

    return HttpResponseRedirect(reverse('event:events'))


@login_required()
def edit(request, eventId):
    event = Events.objects.get(id=eventId)
    event.title = request.POST['title']
    event.text = request.POST['text']
    event.category_id = tools.get_category_id(request, Category)
    event.check = tools.get_check(request)
    event.date = datetime.now()
    event.save()

    return HttpResponseRedirect(reverse('event:events'))


@login_required()
def delete(request, eventId):
    event = Events.objects.get(id=eventId)
    event.delete()

    return HttpResponseRedirect(reverse('event:events'))
