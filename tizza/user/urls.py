from django.urls import path
from .views import SignupView, dashboard, password_reset, password_reset_confirm, edit, edit_password

urlpatterns = [
    path('register/', SignupView.as_view(), name="signup"),
    path('dashboard/', dashboard, name="dashboard"),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset_confirm<str:key>/', password_reset_confirm, name='password_reset_confirm'),
    path('edit/', edit, name='edit'),
    path('edit_password/', edit_password, name='edit_password'),
]