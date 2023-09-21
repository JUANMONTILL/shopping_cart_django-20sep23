from django.contrib import admin
from django.urls import path

from core.views import index, contact

urlpatterns = [
    path('', index, name='index'),
    path('conatact', contact, name='contact'),
    path('admin/', admin.site.urls),
]
