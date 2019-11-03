def get_category(request, model):
    try:
        category = model.objects.get(title=request.POST['category'], user=request.user)
    except:
        model.objects.create(
            user=request.user,
            title=request.POST['category']
        )
        category = model.objects.get(title=request.POST['category'], user=request.user)
    return category


def get_category_id(request, model):
    category = get_category(request, model)
    return category.id


def is_category_available(request, model):
    try:
        category = model.objects.get(title=request.POST['category'], user=request.user)
        return False
    except:
        return True


def get_category_or_false(request, model, categoryId):
    try:
        category = model.objects.get(id=categoryId)
        if request.POST['category'] == category.title:
            return False
    except:
        category = model.objects.get(id=categoryId)
        return category


def get_check(request):
    try:
        check = request.POST['check']
    except:
        check = 'off'
    return check
