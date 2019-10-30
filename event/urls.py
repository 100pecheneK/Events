from django.urls import path

from event.views import event, category

app_name = 'event'
urlpatterns = [
    path('', event.view, name='events'),
    path('category/<int:categoryId>', event.view, name='eventsCat'),
    path('createEvents', event.create, name='create'),
    path('editEvents/<int:eventId>', event.edit, name='edit'),
    path('deleteEvents/<int:eventId>', event.delete, name='delete'),

    path('createCategory', category.create, name='createCategory'),
    path('editCategory/<int:categoryId>', category.edit, name='editCategory'),
    path('deleteCategory/<int:categoryId>', category.delete, name='deleteCategory'),
]
