from django.urls import include, path
from .views import create, update, delete, set_like, set_dislike, remove_like, remove_dislike


urlpatterns = [
    path('create/', create, name='create'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('set_like/<int:pk>/', set_like, name='set_like'),
    path('remove_like/<int:pk>/', remove_like, name='remove_like'),
    path('set_dislike/<int:pk>/', set_dislike, name='set_dislike'),
    path('remove_dislike/<int:pk>/', remove_dislike, name='remove_dislike'),
]