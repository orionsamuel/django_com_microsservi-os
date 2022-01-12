from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Pizza, Pizzeria, Likes, Dislikes
from .forms import PizzaForm


@login_required(login_url='entrar/')
def home(request):
    session = request.session.session_key
    template_name = 'home.html'
    if session:
        content = {}
        search = request.GET.get('search')
        if request.user.is_staff:
            all_pizza = Pizza.objects.filter(creator__owner=request.user)
        else:
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
        content['pizzerias'] = Pizzeria.objects.filter(owner=request.user)
        content['like'], content['dislike'] = like_deslike()
        return render(request, template_name, content)
    else:
        return render(request, 'login.html')


@login_required(login_url='entrar/')
def random(request):
    content = {'pizzas': Pizza.objects.order_by('?')[:5]}
    template_name = 'random.html'
    content['like'], content['dislike'] = like_deslike()
    return render(request, template_name, content)


def like_deslike():
    content = {'likes': Likes.objects.all().values('pizza'),
               'dislikes': Dislikes.objects.all().values('pizza'), 'like': [], 'dislike': []}
    for like in content['likes']:
        for pizza, id in like.items():
            content['like'].append(id)
    for dislike in content['dislikes']:
        for pizza, id in dislike.items():
            content['dislike'].append(id)
    return content['like'], content['dislike']


@login_required(login_url='entrar/')
def create(request):
    form = PizzaForm(request.POST or None)
    if form.is_valid():
        pizza = form.save(commit=False)
        pizza.creator = Pizzeria.objects.get(pk=request.POST["pizza-creator"])
        pizza.save()
        return redirect('home')


@login_required(login_url='entrar/')
def update(request, pk):
    content = {'db': Pizza.objects.get(pk=pk)}
    form = PizzaForm(request.POST or None, instance=content['db'])
    if form.is_valid():
        pizza = form.save(commit=False)
        pizza.creator = Pizzeria.objects.get(pk=request.POST["pizza-creator"])
        pizza.save()
        return redirect('home')


@login_required(login_url='entrar/')
def delete(request, pk):
    db = Pizza.objects.get(pk=pk)
    db.delete()
    return redirect('home')


@login_required(login_url='entrar/')
def set_like(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    new_like = Likes.objects.create(user=request.user, pizza=pizza)
    new_like.save()
    if Dislikes.objects.filter(pizza=pk):
        remove_dislike(request, pk)
    return redirect('home')


@login_required(login_url='entrar/')
def remove_like(request, pk):
    db = Likes.objects.filter(pizza=pk)
    db.delete()
    return redirect('home')


@login_required(login_url='entrar/')
def set_dislike(request, pk):
    pizza = Pizza.objects.get(pk=pk)
    new_dislike = Dislikes.objects.create(user=request.user, pizza=pizza)
    new_dislike.save()
    if Likes.objects.filter(pizza=pk):
        remove_like(request, pk)
    return redirect('home')


@login_required(login_url='entrar/')
def remove_dislike(request, pk):
    db = Dislikes.objects.filter(pizza=pk)
    db.delete()
    return redirect('home')
