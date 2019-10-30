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


def get_check(request):
    try:
        check = request.POST['check']
    except:
        check = 'off'
    return check
