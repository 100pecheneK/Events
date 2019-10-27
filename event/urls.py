from django.urls import path

from . import views

# from category import views as catViews
app_name = 'event'
urlpatterns = [
    path('', views.view, name='events'),
    path('category/<int:cat_id>', views.view, name='eventsCat'),
    path('createEvents', views.create, name='create'),
    path('editEvents/<int:even_id>', views.edit, name='edit'),
    path('deleteEvents/<int:even_id>', views.delete, name='delete'),

    path('createCategory', views.category_create, name='createCategory'),
    path('editCategory/<int:cat_id>', views.category_edit, name='editCategory'),
    path('deleteCategory/<int:cat_id>', views.category_delete, name='deleteCategory'),
]
