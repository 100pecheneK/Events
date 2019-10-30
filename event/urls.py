from django.urls import path

from . import views

# from category import views as catViews
app_name = 'event'
urlpatterns = [
    path('', views.view, name='events'),
    path('category/<int:categoryId>', views.view, name='eventsCat'),
    path('createEvents', views.create, name='create'),
    path('editEvents/<int:eventId>', views.edit, name='edit'),
    path('deleteEvents/<int:eventId>', views.delete, name='delete'),

    path('createCategory', views.category_create, name='createCategory'),
    path('editCategory/<int:categoryId>', views.category_edit, name='editCategory'),
    path('deleteCategory/<int:categoryId>', views.category_delete, name='deleteCategory'),
]
