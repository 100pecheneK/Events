from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico'), name='favicon'),
    path('', include('event.urls')),

    path('accounts/', include('accounts.urls')),

    path('admin/', admin.site.urls),
]
