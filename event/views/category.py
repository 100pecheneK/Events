from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from event.models import Category
from event.tools import tools
from django.contrib import messages


@login_required()
def create(request):
    categoryAvailable = tools.is_category_available(request, Category)
    if categoryAvailable:
        Category.objects.create(
            user=request.user,
            title=request.POST['category']
        )
    else:
        messages.error(request, "Категория уже существует!")
    return HttpResponseRedirect(reverse('event:events'))


@login_required()
def edit(request, categoryId):
    category = tools.get_category_or_false(request, Category, categoryId)
    if category:
        category.title = request.POST['title']
        category.save()
    else:
        messages.error(request, "Категория уже существует!")

    return HttpResponseRedirect(reverse('event:events'))


@login_required()
def delete(request, categoryId):
    category = Category.objects.get(id=categoryId)
    category.delete()

    return HttpResponseRedirect(reverse('event:events'))
