from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .forms import RegisterForm


class SignupView(View):
    template_name = 'signup.html'

    @staticmethod
    def post(request):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/pizzas/7')

    def get(self, request):
        return render(request, self.template_name, {'form': RegisterForm()})
