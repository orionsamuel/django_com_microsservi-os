from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, authenticate
from django.views import View
from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset
from django.contrib.auth.decorators import login_required


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
            return redirect('home')

    def get(self, request):
        return render(request, self.template_name, {'form': RegisterForm()})


@login_required(login_url='entrar/')
def dashboard(request):
    template_name = 'dashboard.html'
    return render(request, template_name)


def password_reset(request):
    template_name = 'password_reset.html'
    content = {}
    form = PasswordResetForm(request.POST or None)
    if form.is_valid():
        form.save()
        content['success'] = True
        return redirect('login')
    content['form'] = form
    return render(request, template_name, content)


def password_reset_confirm(request, key):
    template_name = 'password_reset_confirm.html'
    content = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        content['success'] = True
        user = authenticate(username=reset.user, password=form.cleaned_data['new_password1'])
        login(request, user)
        return redirect('home')
    content['form'] = form
    return render(request, template_name, content)


@login_required(login_url='entrar/')
def edit(request):
    template_name = 'edit.html'
    content = {}
    form = EditAccountForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        form = EditAccountForm(instance=request.user)
        content['success'] = True
    content['form'] = form
    return render(request, template_name, content)


@login_required(login_url='entrar/')
def edit_password(request):
    template_name = 'edit_password.html'
    content = {}
    form = PasswordChangeForm(data=request.POST or None, user=request.user)
    if form.is_valid():
        form.save()
        content['success'] = True
        username = request.user
        password = form.cleaned_data['new_password1']
        user = authenticate(username=username, password=password)
        login(request, user)
    content['form'] = form
    return render(request, template_name, content)
