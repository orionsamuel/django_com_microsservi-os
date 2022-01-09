from django.urls import include, path
from .views import create


urlpatterns = [
    path('create/', create, name='create')
]