from django import views
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect

from accounts import forms


class CustomLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

    def get_default_redirect_url(self):
        messages.success(self.request, 'You have successfully logged in')
        return super().get_default_redirect_url()


class CustomLogoutView(LogoutView):
    template_name = "accounts/logout.html"

    def get_default_redirect_url(self):
        messages.success(self.request, 'You have successfully logout')
        return super().get_default_redirect_url()


class RegisterView(views.View):

    def get(self, request):
        form = forms.RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('posts:home')
        return render(request, 'accounts/register.html', {'form': form})
