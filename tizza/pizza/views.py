from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Pizza, Pizzeria, Likes
from .forms import PizzaForm


@login_required(login_url='entrar/')
def home(request):
    session = request.session.session_key
    template_name = 'home.html'
    if session:
        content = {}
        search = request.GET.get('search')
        all_pizza = Pizza.objects.all()
        paginator = Paginator(all_pizza, 10)
        pages = request.GET.get('page')
        content['pizzas'] = paginator.get_page(pages)
        if search:
            content['pizzas'] = Pizza.objects.filter(title__icontains=search)
            paginator_src = Paginator(content['pizzas'], 10)
            content['paginator'] = paginator_src.get_page(pages)
        else:
            content['paginator'] = paginator.get_page(pages)
        content['form'] = PizzaForm()
        return render(request, template_name, content)
    else:
        return render(request, 'login.html')


@login_required(login_url='entrar/')
def create(request):
    form = PizzaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')


@login_required(login_url='entrar/')
def update(request, pk):
    content = {'db': Pizza.objects.get(pk=pk)}
    form = PizzaForm(request.POST or None, instance=content['db'])
    if form.is_valid():
        form.save()
        return redirect('home')


@login_required(login_url='entrar/')
def delete(request, pk):
    db = Pizza.objects.get(pk=pk)
    db.delete()
    return redirect('home')
