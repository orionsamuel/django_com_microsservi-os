from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Pizza

def index(request, pid):
    pizza = get_object_or_404(Pizza, id=pid)
    content = {
        'id': pizza.id,
        'title': pizza.title,
        'description': pizza.description,
        'type': pizza.type,
    }
    return JsonResponse(content)