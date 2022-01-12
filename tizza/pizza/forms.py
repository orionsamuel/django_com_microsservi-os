from django import forms
from .models import Pizza, Pizzeria
from user.models import UserProfile

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['title', 'description', 'type']