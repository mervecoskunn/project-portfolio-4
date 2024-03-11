from django import views
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from accounts.forms import RegisterForm


class RegisterView(views.View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('posts:home')
        return render(request, 'accounts/register.html', {'form': form})
