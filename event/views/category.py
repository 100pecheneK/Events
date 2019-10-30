from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from event.models import Category


@login_required()
def create(request):
    # TODO Добавить валидацию (нельзя создавать одинаковые категории)
    Category.objects.create(
        user=request.user,
        title=request.POST['category']
    )

    return HttpResponseRedirect(reverse('event:events'))


@login_required()
def edit(request, categoryId):
    category = Category.objects.get(id=categoryId)
    # TODO Добавить валидацию (нельзя создавать одинаковые категории)
    category.title = request.POST['title']
    category.save()

    return HttpResponseRedirect(reverse('event:events'))


@login_required()
def delete(request, categoryId):
    category = Category.objects.get(id=categoryId)
    category.delete()

    return HttpResponseRedirect(reverse('event:events'))
