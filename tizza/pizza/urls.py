from django.urls import include, path
from .views import create, update, delete


urlpatterns = [
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
]