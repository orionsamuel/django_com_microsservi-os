from django.contrib import admin
from .models import Pizza, Pizzeria


class PizzaAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'creator']
    search_fields = ['title']


class PizzeriaAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'address']
    search_fields = ['name']


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(Pizzeria, PizzeriaAdmin)